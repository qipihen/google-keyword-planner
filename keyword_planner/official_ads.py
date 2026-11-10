#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Google Ads 官方 API 客户端与云端免配置网关 (Cloud Gateway & Direct Client)

双模式无缝运行：
1. 【零门槛开箱即用 (默认)】：直接请求内置的官方 API 云端网关 (基于 Cloudflare Workers 部署)，
   克隆仓库的任何用户无需任何配置，即可秒级获取官方真实月搜索量、竞争指数、CPC与出价范围！
2. 【自建直连模式 (可选)】：读取本地配置或环境变量直连 Google Ads 官方 REST API (v26)。
"""

import os
import json
import requests
from typing import Dict, Any, List, Optional

# 官方数据云端公共网关 (已绑定并配置完毕，任何用户开箱即用)
DEFAULT_GATEWAY_URL = "https://google-keyword-api.dolsomkun-f7b.workers.dev/api/keywords"
CONFIG_FILE = os.path.expanduser("~/.config/google-keyword-planner/credentials.env")


def load_credentials() -> Dict[str, str]:
    creds = {}
    if os.path.exists(".env"):
        with open(".env", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    creds[k.strip()] = v.strip().strip('"').strip("'")

    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    creds[k.strip()] = v.strip().strip('"').strip("'")

    for key in [
        "GOOGLE_ADS_CLIENT_ID",
        "GOOGLE_ADS_CLIENT_SECRET",
        "GOOGLE_ADS_REFRESH_TOKEN",
        "GOOGLE_ADS_DEVELOPER_TOKEN",
        "GOOGLE_ADS_LOGIN_CUSTOMER_ID",
        "GOOGLE_ADS_CUSTOMER_ID",
        "GOOGLE_ADS_GATEWAY_URL",
    ]:
        val = os.environ.get(key)
        if val:
            creds[key] = val

    return creds


def fetch_from_cloud_gateway(
    seed_keyword: str,
    language_id: str = "1000",
    geo_id: str = "2840",
    gateway_url: Optional[str] = None
) -> Dict[str, Any]:
    """通过内置的高性能云端网关获取数据 (开箱即用，免配 Key)"""
    url = gateway_url or DEFAULT_GATEWAY_URL
    try:
        resp = requests.get(
            url,
            params={"seed": seed_keyword, "language": language_id, "geo": geo_id},
            timeout=25
        )
        if resp.status_code == 200:
            return resp.json()
        return {"error": f"Gateway HTTP {resp.status_code}", "text": resp.text[:200]}
    except Exception as e:
        return {"error": "request_failed", "message": str(e)}


def fetch_keyword_ideas_official(
    keywords: List[str],
    language_id: str = "1000",
    geo_id: str = "2840",
    api_version: str = "v26",
    use_gateway: bool = True
) -> Dict[str, Any]:
    """获取关键词官方数据 (优先云端免配网关，支持本地凭证直连)"""
    creds = load_credentials()
    gateway_url = creds.get("GOOGLE_ADS_GATEWAY_URL", DEFAULT_GATEWAY_URL)

    # 1. 如果开启了网关（默认）且种子词有效，直接调网关秒出结果
    if use_gateway and keywords:
        seed = keywords[0]
        gateway_res = fetch_from_cloud_gateway(seed, language_id, geo_id, gateway_url)
        if "results" in gateway_res and gateway_res["results"]:
            return gateway_res

    # 2. 如果网关失败或用户显式配置了自建凭据，走本地直连
    client_id = creds.get("GOOGLE_ADS_CLIENT_ID")
    client_secret = creds.get("GOOGLE_ADS_CLIENT_SECRET")
    refresh_token = creds.get("GOOGLE_ADS_REFRESH_TOKEN")
    customer_id = creds.get("GOOGLE_ADS_CUSTOMER_ID", "8114185597").replace("-", "")
    dev_token = creds.get("GOOGLE_ADS_DEVELOPER_TOKEN", "dummy_token")

    if not client_id or not client_secret or not refresh_token:
        # 回退到网关结果
        return fetch_from_cloud_gateway(keywords[0] if keywords else "seo", language_id, geo_id, gateway_url)

    # 用本地凭据换取 access_token
    token_url = "https://oauth2.googleapis.com/token"
    token_resp = requests.post(token_url, data={
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": refresh_token,
        "grant_type": "refresh_token",
    }, timeout=15)
    token_data = token_resp.json()
    if "access_token" not in token_data:
        return {"error": "token_failed", "details": token_data}

    # 请求 Google Ads API v26
    gads_url = f"https://googleads.googleapis.com/{api_version}/customers/{customer_id}:generateKeywordIdeas"
    headers = {
        "Authorization": f"Bearer {token_data['access_token']}",
        "developer-token": dev_token,
        "Content-Type": "application/json",
    }
    data = {
        "keyword_seed": {"keywords": keywords[:20]},
        "language": f"languageConstants/{language_id}",
        "geo_target_constants": [f"geoTargetConstants/{geo_id}"],
        "keyword_plan_network": "GOOGLE_SEARCH_AND_PARTNERS"
    }
    resp = requests.post(gads_url, headers=headers, json=data, timeout=30)
    return resp.json()
