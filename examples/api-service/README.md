# API Service - REST API 服务

> 使用 Vibe Coding 方法创建的完整 REST API 服务，包含认证、CRUD 操作和最佳实践

## 📖 项目介绍

这是一个功能完整的 REST API 服务示例，展示了如何使用 Vibe Coding 方法开发一个包含用户认证、数据验证、错误处理和 API 文档的完整后端服务。项目使用 Flask 和 SQLite，遵循 RESTful 设计原则。

## 🎯 项目功能

### 核心功能
- ✅ RESTful API 设计
- ✅ 用户注册和登录
- ✅ JWT 令牌认证
- ✅ 资源 CRUD 操作（产品管理示例）
- ✅ 数据验证和错误处理
- ✅ API 文档（Swagger/OpenAPI）
- ✅ 分页和筛选
- ✅ 请求日志记录

### 安全特性
- ✅ 密码加密存储
- ✅ JWT 令牌认证
- ✅ 请求限流
- ✅ 输入验证和清理
- ✅ CORS 配置

## 🏗️ 项目结构

```
api-service/
├── README.md              # 项目说明
├── requirements.txt       # Python 依赖
├── app.py                 # Flask 主程序
├── models.py              # 数据模型
├── database.py            # 数据库操作
├── auth.py                # 认证模块
├── validators.py          # 数据验证
├── config.py              # 配置文件
└── tests/                 # 测试文件
    └── test_api.py        # API 测试
```

## 🚀 如何使用 Vibe Coding 创建这个项目

### 步骤 1: 项目初始化

在 Cursor 中：

1. 创建项目文件夹 `api-service`
2. 按 `Cmd/Ctrl + I` 打开 AI 对话面板
3. 输入：
   ```
   我想创建一个 REST API 服务，使用 Flask。
   请帮我创建项目结构，包括：
   - app.py（Flask 主程序）
   - models.py（数据模型）
   - database.py（数据库操作）
   - auth.py（认证模块）
   - requirements.txt（依赖文件）
   ```

### 步骤 2: 实现认证系统

```
请实现用户认证功能：
1. 用户注册（POST /api/auth/register）
2. 用户登录（POST /api/auth/login）
3. JWT 令牌生成和验证
4. 密码加密存储（使用 bcrypt）
5. 受保护的路由中间件
```

### 步骤 3: 实现资源 API

```
请实现产品管理 API：
1. GET /api/products - 获取产品列表（支持分页和筛选）
2. GET /api/products/<id> - 获取单个产品
3. POST /api/products - 创建产品（需要认证）
4. PUT /api/products/<id> - 更新产品（需要认证）
5. DELETE /api/products/<id> - 删除产品（需要认证）
```

### 步骤 4: 添加数据验证和错误处理

```
请添加：
1. 输入数据验证（使用 validators）
2. 统一的错误处理机制
3. API 响应格式标准化
4. 请求日志记录
```

## 💻 运行项目

### 安装依赖

```bash
pip install -r requirements.txt
```

### 初始化数据库

```bash
python database.py
```

### 启动服务器

```bash
python app.py
```

API 服务运行在 `http://localhost:5000`

## 📝 API 文档

### 认证端点

#### 用户注册

```http
POST /api/auth/register
Content-Type: application/json

{
  "username": "user123",
  "email": "user@example.com",
  "password": "securepassword"
}
```

响应：
```json
{
  "message": "用户注册成功",
  "user": {
    "id": 1,
    "username": "user123",
    "email": "user@example.com"
  }
}
```

#### 用户登录

```http
POST /api/auth/login
Content-Type: application/json

{
  "username": "user123",
  "password": "securepassword"
}
```

响应：
```json
{
  "message": "登录成功",
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "user": {
    "id": 1,
    "username": "user123",
    "email": "user@example.com"
  }
}
```

### 产品端点

#### 获取产品列表

```http
GET /api/products?page=1&per_page=10&category=电子产品&min_price=100&max_price=1000
Authorization: Bearer <token>
```

响应：
```json
{
  "products": [...],
  "total": 50,
  "page": 1,
  "per_page": 10,
  "pages": 5
}
```

#### 获取单个产品

```http
GET /api/products/1
Authorization: Bearer <token>
```

#### 创建产品

```http
POST /api/products
Authorization: Bearer <token>
Content-Type: application/json

{
  "name": "iPhone 15",
  "description": "最新款 iPhone",
  "price": 7999,
  "category": "电子产品",
  "stock": 100
}
```

#### 更新产品

```http
PUT /api/products/1
Authorization: Bearer <token>
Content-Type: application/json

{
  "price": 7499,
  "stock": 80
}
```

#### 删除产品

```http
DELETE /api/products/1
Authorization: Bearer <token>
```

## 🔐 认证说明

大部分 API 端点需要 JWT 令牌认证。在请求头中添加：

```
Authorization: Bearer <your_jwt_token>
```

## 🎨 技术栈

- **后端框架**: Flask
- **数据库**: SQLite
- **认证**: JWT (PyJWT)
- **密码加密**: bcrypt
- **API 文档**: Flask-RESTX (可选)

## 📚 学习要点

通过这个项目，你学会了：

1. **RESTful API 设计**：遵循 REST 原则设计 API
2. **认证和授权**：实现 JWT 令牌认证系统
3. **数据验证**：输入数据的验证和清理
4. **错误处理**：统一的错误响应格式
5. **安全实践**：密码加密、令牌验证、输入验证
6. **API 文档**：编写清晰的 API 文档

## 🔄 扩展功能建议

完成基础功能后，可以尝试添加：

- 角色和权限管理（RBAC）
- API 版本控制
- 请求限流和防刷
- 数据缓存（Redis）
- 文件上传功能
- 邮件通知
- API 监控和日志分析
- 单元测试和集成测试
- Docker 容器化
- CI/CD 流程

## 💡 Vibe Coding 技巧

1. **模块化设计**：将功能拆分为独立模块，便于维护
2. **安全优先**：始终考虑安全性，让 AI 添加安全措施
3. **错误处理**：完善的错误处理提升 API 可用性
4. **文档完善**：清晰的 API 文档便于使用和维护
5. **测试驱动**：编写测试确保 API 功能正确

## 🧪 测试 API

### 使用 curl

```bash
# 注册用户
curl -X POST http://localhost:5000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","email":"test@example.com","password":"test123"}'

# 登录
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"test123"}'

# 获取产品列表（需要 token）
curl -X GET http://localhost:5000/api/products \
  -H "Authorization: Bearer <your_token>"
```

### 使用 Postman

1. 导入 API 集合
2. 先调用注册/登录接口获取 token
3. 在环境变量中设置 token
4. 测试其他需要认证的接口

---

**祝你学习愉快！** 🚀

返回 [Vibe Coding 初学者指南](../../tutorials/vibe-coding/beginner-guide.md)
