# Google Ads API 常见问题与排错手册

### 1. `UNAUTHENTICATED` / 401
- **原因**：Access Token 已失效，或客户端密钥与授权账号不一致。
- **解决**：运行 `python run.py --setup` 重新授权即可。

### 2. `USER_DOES_NOT_HAVE_ACCESS`
- **原因**：授权的 Gmail 邮箱在填写的 MCC 经理账号或客户账号中没有权限。
- **解决**：登录 Google Ads -> 管理 -> 访问权限和安全，确保授权的 Gmail 邮箱在用户列表中。

### 3. `CUSTOMER_NOT_FOUND` / 404
- **原因**：Customer ID 填写了连字符 `-` 或数字错误。
- **解决**：账号 ID 必须为纯 10 位数字（例如 `8114185597`，而不是 `811-418-5597`）。

### 4. 为什么免配置模式不需要任何 Key？
- 默认的免 Token 模式直接采用经过词边界清洗的 Google Autocomplete 引擎，100% 免费，适合任何刚克隆仓库的用户秒级开箱使用。
