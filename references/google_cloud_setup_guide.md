# Google Cloud 与 Google Ads 凭证自建指南 (完全免费)

本项目支持完全无需配置的**免费极速模式**；若你需要调用 Google 官方 Ads 数据获取精确搜索量与 CPC，可按照本指南在 2 分钟内创建你专属的客户端密钥。

---

## 步骤一：创建项目并启用 Google Ads API

1. 登录 [Google Cloud Console](https://console.cloud.google.com/)。
2. 顶部下拉框点击 **新建项目 (New Project)**，命名为 `keyword-planner`。
3. 左侧导航进入 **API 和服务 -> 库 (Library)**，搜索 `Google Ads API` 并点击 **启用 (Enable)**。

---

## 步骤二：配置 OAuth 同意屏幕

1. 进入 **API 和服务 -> OAuth 同意屏幕 (OAuth consent screen)**。
2. 类型选择 **外部 (External)**，点击创建。
3. 填入应用名（如 `Keyword Planner Client`）和你的联系邮箱。
4. 测试用户 (Test Users) 区域：**添加你登录 Google Ads 的 Gmail 账号**。

---

## 步骤三：创建 OAuth 2.0 客户端密钥

1. 进入 **API 和服务 -> 凭据 (Credentials)**。
2. 点击 **创建凭据 -> OAuth 客户端 ID**。
3. 应用类型选择：**桌面应用 (Desktop app)**，名称自定义。
4. 点击创建后，复制生成的 **Client ID** 与 **Client Secret**。

---

## 步骤四：一键运行本地授权向导

在终端中运行：
```bash
python run.py --setup
```
向导会自动启动本地授权通道（`http://127.0.0.1:8787`），并在浏览器中打开授权页，确认后**自动将长期有效的 `refresh_token` 保存至本地配置**，后续无需重复操作。
