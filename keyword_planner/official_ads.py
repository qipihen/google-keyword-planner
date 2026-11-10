#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Google Ads 官方 REST API 直连模块 (Official Ads API Client)
完全使用用户自建凭证，零第三方中介，支持批量获取官方真实搜索量、竞争指数、CPC与12个月趋势。
"""

import os
import json
import requests
from typing import Dict, Any, List, Optional

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
    ]:
        val = os.environ.get(key)
        if val:
            creds[key] = val

    return creds


def get_access_token(client_id: str, client_secret: str, refresh_token: str) -> str:
    token_url = "https://oauth2.googleapis.com/token"
    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": refresh_token,
        "grant_type": "refresh_token",
    }
    resp = requests.post(token_url, data=payload, timeout=15)
    data = resp.json()
    if "access_token" not in data:
        raise RuntimeError(f"换取 access_token 失败:\n{json.dumps(data, ensure_ascii=False, indent=2)}")
    return data["access_token"]


def fetch_keyword_ideas_official(
    keywords: List[str],
    language_id: str = "1000",
    geo_id: str = "2840",
    api_version: str = "v18"
) -> Dict[str, Any]:
    creds = load_credentials()
    client_id = creds.get("GOOGLE_ADS_CLIENT_ID")
    client_secret = creds.get("GOOGLE_ADS_CLIENT_SECRET")
    refresh_token = creds.get("GOOGLE_ADS_REFRESH_TOKEN")
    customer_id = creds.get("GOOGLE_ADS_CUSTOMER_ID", "").replace("-", "")
    login_id = creds.get("GOOGLE_ADS_LOGIN_CUSTOMER_ID", "").replace("-", "")
    dev_token = creds.get("GOOGLE_ADS_DEVELOPER_TOKEN", "")

    if not client_id or not client_secret or not refresh_token or not customer_id:
        return {"error": "missing_credentials", "message": "尚未配置 Google Ads API 凭据，请运行 python run.py --setup 启动向导。"}

    access_token = get_access_token(client_id, client_secret, refresh_token)
    url = f"https://googleads.googleapis.com/{api_version}/customers/{customer_id}:generateKeywordIdeas"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    if dev_token:
        headers["developer-token"] = dev_token
    if login_id:
        headers["login-customer-id"] = login_id

    data = {
        "keyword_seed": {"keywords": keywords[:20]},
        "language": f"languageConstants/{language_id}",
        "geo_target_constants": [f"geoTargetConstants/{geo_id}"],
        "keyword_plan_network": "GOOGLE_SEARCH_AND_PARTNERS"
    }

    resp = requests.post(url, headers=headers, json=data, timeout=30)
    return resp.json()
