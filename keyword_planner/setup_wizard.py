#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Google Ads API 交互式开箱配置向导 (Zero-Friction Setup Wizard)
帮助任何开发者或 SEO 人员在 2 分钟内完成自建 Google Cloud 凭证与 OAuth 授权。
"""

import os
import sys
import json
import urllib.parse
import webbrowser
import http.server
import socketserver
import requests

CONFIG_DIR = os.path.expanduser("~/.config/google-keyword-planner")
CONFIG_FILE = os.path.join(CONFIG_DIR, "credentials.env")


def run_setup():
    os.makedirs(CONFIG_DIR, exist_ok=True)
    print("=" * 68)
    print("🌟 Google Ads API 凭据配置向导 (Google Keyword Planner Setup)")
    print("=" * 68)
    print("通过配置自己的凭证，你将拥有每天 15,000 次免费官方关键词查询额度！")
    print("如果还没有 Client ID，请参考 references/google_cloud_setup_guide.md 创建桌面凭据。\n")

    current = {}
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    current[k.strip()] = v.strip().strip('"').strip("'")

    # 1. Client ID
    def_cid = current.get("GOOGLE_ADS_CLIENT_ID", "")
    p_cid = f"1. 请输入 OAuth 2.0 Client ID [{def_cid[:15]}...]: " if def_cid else "1. 请输入 OAuth 2.0 Client ID: "
    client_id = input(p_cid).strip() or def_cid
    if not client_id:
        print("❌ Client ID 不能为空")
        return

    # 2. Client Secret
    def_sec = current.get("GOOGLE_ADS_CLIENT_SECRET", "")
    p_sec = "2. 请输入 Client Secret [已保存]: " if def_sec else "2. 请输入 Client Secret: "
    client_secret = input(p_sec).strip() or def_sec
    if not client_secret:
        print("❌ Client Secret 不能为空")
        return

    # 3. Refresh Token
    refresh_token = current.get("GOOGLE_ADS_REFRESH_TOKEN", "")
    reauth = True
    if refresh_token:
        choice = input("已存在 Refresh Token，是否重新授权？(y/N): ").strip().lower()
        if choice not in ["y", "yes"]:
            reauth = False

    if reauth:
        redirect_uri = "http://127.0.0.1:8787"
        scope = "https://www.googleapis.com/auth/adwords"
        auth_url = (
            f"https://accounts.google.com/o/oauth2/v2/auth?"
            f"client_id={urllib.parse.quote(client_id)}&"
            f"redirect_uri={urllib.parse.quote(redirect_uri)}&"
            f"response_type=code&"
            f"scope={urllib.parse.quote(scope)}&"
            f"access_type=offline&"
            f"prompt=consent"
        )
        print("\n" + "-" * 60)
        print("🔑 正在唤起本地授权监听...")
        print(f"授权地址: {auth_url}")
        print("-" * 60 + "\n")
        try:
            webbrowser.open(auth_url)
        except Exception:
            pass

        auth_code = None

        class Handler(http.server.SimpleHTTPRequestHandler):
            def do_GET(self):
                nonlocal auth_code
                p = urllib.parse.urlparse(self.path)
                params = urllib.parse.parse_qs(p.query)
                if "code" in params:
                    auth_code = params["code"][0]
                    self.send_response(200)
                    self.send_header("Content-type", "text/html; charset=utf-8")
                    self.end_headers()
                    self.wfile.write("<h1>✅ 授权成功！您可以关闭此窗口返回终端。</h1>".encode("utf-8"))
                else:
                    self.send_response(400)
                    self.end_headers()
                    self.wfile.write(b"Failed.")

            def log_message(self, format, *args):
                pass

        try:
            with socketserver.TCPServer(("127.0.0.1", 8787), Handler) as httpd:
                print("⏳ 等待浏览器授权回调...")
                httpd.handle_request()
        except Exception:
            auth_code = input("无法自动监听，请粘贴重定向 URL 里的 code 值: ").strip()

        if not auth_code:
            print("❌ 未获得授权码")
            return

        token_url = "https://oauth2.googleapis.com/token"
        resp = requests.post(token_url, data={
            "client_id": client_id,
            "client_secret": client_secret,
            "code": auth_code,
            "grant_type": "authorization_code",
            "redirect_uri": redirect_uri
        })
        res_data = resp.json()
        if "refresh_token" in res_data:
            refresh_token = res_data["refresh_token"]
            print("🎉 成功获取 Refresh Token！")
        else:
            print(f"❌ 换取失败: {res_data}")
            return

    # 4. MCC ID & Customer ID
    def_mcc = current.get("GOOGLE_ADS_LOGIN_CUSTOMER_ID", "")
    mcc_id = input(f"3. 请输入 Google Ads 经理账号 (MCC) ID 10位数字 [{def_mcc}]: ").strip().replace("-", "") or def_mcc

    def_cid = current.get("GOOGLE_ADS_CUSTOMER_ID", "")
    cid = input(f"4. 请输入目标客户广告账号 ID 10位数字 [{def_cid}]: ").strip().replace("-", "") or def_cid or mcc_id

    def_dev = current.get("GOOGLE_ADS_DEVELOPER_TOKEN", "")
    dev_token = input(f"5. 请输入 Developer Token (选填直接回车) [{def_dev}]: ").strip() or def_dev

    config = {
        "GOOGLE_ADS_CLIENT_ID": client_id,
        "GOOGLE_ADS_CLIENT_SECRET": client_secret,
        "GOOGLE_ADS_REFRESH_TOKEN": refresh_token,
        "GOOGLE_ADS_LOGIN_CUSTOMER_ID": mcc_id,
        "GOOGLE_ADS_CUSTOMER_ID": cid,
        "GOOGLE_ADS_DEVELOPER_TOKEN": dev_token,
    }

    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        f.write("# Google Keyword Planner Credentials\n")
        for k, v in config.items():
            f.write(f'{k}="{v}"\n')

    print(f"\n💾 配置已安全存储至: {CONFIG_FILE}")
    print("=" * 68)


if __name__ == "__main__":
    run_setup()
