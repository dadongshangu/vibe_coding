# Vibe Coding 实战项目案例

> 通过真实项目案例，学习如何使用 Vibe Coding 完成完整的产品开发

## 📖 目录

1. [项目一：个人博客网站](#项目一个人博客网站)
2. [项目二：任务管理应用](#项目二任务管理应用)
3. [项目三：REST API 服务](#项目三rest-api-服务)
4. [项目四：实时聊天应用](#项目四实时聊天应用)
5. [经验总结](#经验总结)

---

## 项目一：个人博客网站

### 项目概述

**目标**：创建一个功能完整的个人博客网站，支持文章发布、分类、评论等功能。

**技术栈**：
- 后端：Node.js + Express + MongoDB
- 前端：React + Next.js
- 样式：Tailwind CSS
- 部署：Vercel

### 开发过程

#### 阶段 1：需求分析和规划

**Prompt**：
```
创建一个个人博客系统，包含以下功能：

【核心功能】
1. 文章管理
   - 创建、编辑、删除文章
   - 支持 Markdown 格式
   - 文章分类和标签
   - 文章状态（草稿/发布）

2. 用户系统
   - 注册、登录
   - 个人资料管理
   - 权限控制（管理员/普通用户）

3. 前端展示
   - 文章列表（分页、分类筛选）
   - 文章详情页
   - 搜索功能
   - 响应式设计

【技术要求】
- 使用 Next.js 做 SSR
- SEO 优化
- 代码规范：ESLint + Prettier
```

#### 阶段 2：项目结构搭建

**Prompt**：
```
创建项目结构：

blog-system/
├── backend/
│   ├── models/      # 数据模型
│   ├── routes/      # 路由
│   ├── controllers/ # 控制器
│   ├── middleware/  # 中间件
│   └── utils/       # 工具函数
├── frontend/
│   ├── components/  # 组件
│   ├── pages/       # 页面
│   ├── styles/      # 样式
│   └── utils/       # 工具函数
└── shared/          # 共享代码

请创建基础的项目结构和配置文件。
```

#### 阶段 3：数据模型设计

**Prompt**：
```
设计博客系统的数据模型：

1. User 模型
   - id, email, password, name, role, createdAt

2. Article 模型
   - id, title, content, author, category, tags, status, createdAt, updatedAt

3. Category 模型
   - id, name, description

使用 MongoDB + Mongoose，包含数据验证。
```

#### 阶段 4：后端 API 开发

**Prompt**：
```
创建文章管理的 REST API：

GET    /api/articles        # 获取文章列表（支持分页、筛选）
GET    /api/articles/:id    # 获取单篇文章
POST   /api/articles        # 创建文章（需要认证）
PUT    /api/articles/:id    # 更新文章（需要认证）
DELETE /api/articles/:id    # 删除文章（需要认证）

要求：
- 使用 JWT 认证
- 输入验证
- 错误处理
- 返回统一的 JSON 格式
```

#### 阶段 5：前端页面开发

**Prompt**：
```
创建博客前端页面：

1. 首页（文章列表）
   - 显示最新文章
   - 分页
   - 分类筛选
   - 搜索功能

2. 文章详情页
   - 显示文章内容（Markdown 渲染）
   - 相关文章推荐
   - 响应式设计

3. 管理后台
   - 文章列表
   - 创建/编辑文章
   - 使用富文本编辑器

使用 Next.js + Tailwind CSS
```

#### 阶段 6：功能完善

**Prompt**：
```
完善博客功能：

1. 添加评论系统
   - 用户可以评论文章
   - 支持回复评论
   - 评论审核（管理员）

2. SEO 优化
   - 添加 meta 标签
   - 生成 sitemap
   - 结构化数据

3. 性能优化
   - 图片懒加载
   - 文章列表分页
   - 静态页面生成
```

### 遇到的问题和解决方案

#### 问题 1：Markdown 渲染性能

**问题**：文章内容很长时，Markdown 渲染很慢

**解决方案 Prompt**：
```
优化 Markdown 渲染性能：
- 使用服务端渲染
- 添加缓存
- 代码高亮使用异步加载
```

#### 问题 2：图片上传

**问题**：需要支持图片上传

**解决方案 Prompt**：
```
添加图片上传功能：
- 使用云存储（如 Cloudinary）
- 图片压缩
- 支持多种格式
- 返回图片 URL
```

### 项目成果

- ✅ 完整的博客系统
- ✅ 支持文章 CRUD
- ✅ 用户认证和权限
- ✅ SEO 优化
- ✅ 响应式设计
- ✅ 部署到生产环境

---

## 项目二：任务管理应用

### 项目概述

**目标**：创建一个功能丰富的任务管理应用，类似 Trello。

**技术栈**：
- 前端：React + TypeScript
- 状态管理：Redux Toolkit
- 后端：Node.js + Express
- 数据库：PostgreSQL
- 实时更新：WebSocket

### 开发过程

#### 阶段 1：需求分析

**Prompt**：
```
创建一个任务管理应用（类似 Trello）：

【核心功能】
1. 看板（Board）
   - 创建多个看板
   - 看板可以共享

2. 列表（List）
   - 在看板中创建多个列表
   - 可以拖拽排序

3. 任务（Card）
   - 在列表中创建任务
   - 任务可以拖拽移动
   - 任务详情（描述、截止日期、标签、成员）

4. 用户协作
   - 邀请成员
   - 实时更新
   - 活动日志

【技术要求】
- 使用 TypeScript
- 实时同步（WebSocket）
- 拖拽功能（react-beautiful-dnd）
```

#### 阶段 2：数据模型

**Prompt**：
```
设计任务管理系统的数据模型：

1. Board（看板）
   - id, name, description, owner, members, createdAt

2. List（列表）
   - id, boardId, name, order, createdAt

3. Card（任务）
   - id, listId, title, description, dueDate, labels, members, order

4. User（用户）
   - id, email, name, avatar

使用 PostgreSQL + Prisma ORM
```

#### 阶段 3：拖拽功能实现

**Prompt**：
```
实现任务拖拽功能：

要求：
- 可以在列表内拖拽排序
- 可以拖拽到其他列表
- 拖拽后更新数据库
- 实时同步给其他用户
- 使用 react-beautiful-dnd

处理：
- 拖拽开始/结束事件
- 更新本地状态
- 发送到服务器
- 错误回滚
```

#### 阶段 4：实时同步

**Prompt**：
```
实现实时同步功能：

使用 WebSocket：
- 用户操作（创建、更新、删除）实时同步
- 多用户同时编辑处理冲突
- 显示在线用户
- 活动日志实时更新

要求：
- 使用 Socket.io
- 处理连接断开重连
- 优化消息频率
```

### 遇到的问题和解决方案

#### 问题 1：拖拽冲突

**问题**：多用户同时拖拽导致冲突

**解决方案 Prompt**：
```
解决拖拽冲突：
- 使用乐观更新
- 服务器端验证
- 冲突时使用服务器状态
- 显示冲突提示
```

#### 问题 2：性能问题

**问题**：看板任务很多时，页面卡顿

**解决方案 Prompt**：
```
优化性能：
- 虚拟滚动（react-window）
- 按需加载任务详情
- 使用 React.memo 优化组件
- 减少不必要的重渲染
```

---

## 项目三：REST API 服务

### 项目概述

**目标**：创建一个 RESTful API 服务，提供用户、商品、订单等管理功能。

**技术栈**：
- 框架：Node.js + Express
- 数据库：PostgreSQL
- ORM：Prisma
- 认证：JWT
- 文档：Swagger

### 开发过程

#### 阶段 1：API 设计

**Prompt**：
```
设计一个电商 REST API：

【资源设计】
1. Users（用户）
   GET    /api/users
   GET    /api/users/:id
   POST   /api/users
   PUT    /api/users/:id
   DELETE /api/users/:id

2. Products（商品）
   GET    /api/products
   GET    /api/products/:id
   POST   /api/products
   PUT    /api/products/:id
   DELETE /api/products/:id

3. Orders（订单）
   GET    /api/orders
   GET    /api/orders/:id
   POST   /api/orders
   PUT    /api/orders/:id

【要求】
- 遵循 RESTful 规范
- 统一的响应格式
- 完整的错误处理
- API 文档（Swagger）
```

#### 阶段 2：认证和授权

**Prompt**：
```
实现 JWT 认证系统：

功能：
- 用户注册（邮箱验证）
- 用户登录（返回 token）
- Token 刷新
- 密码重置

安全要求：
- 密码加密（bcrypt）
- Token 过期时间（1小时）
- Refresh token（7天）
- 速率限制
- 输入验证
```

#### 阶段 3：数据验证

**Prompt**：
```
添加数据验证：

使用 Joi 或 express-validator：
- 请求参数验证
- 请求体验证
- 自定义验证规则
- 友好的错误信息

示例：
- 邮箱格式验证
- 密码强度验证
- 数字范围验证
- 必填字段验证
```

#### 阶段 4：API 文档

**Prompt**：
```
生成 Swagger API 文档：

要求：
- 所有端点都有文档
- 请求/响应示例
- 错误响应说明
- 认证说明
- 可以交互测试
```

### 遇到的问题和解决方案

#### 问题 1：分页性能

**问题**：大量数据时分页查询慢

**解决方案 Prompt**：
```
优化分页查询：
- 使用游标分页（cursor-based）
- 添加数据库索引
- 限制最大页数
- 使用缓存
```

#### 问题 2：API 版本控制

**问题**：需要支持 API 版本

**解决方案 Prompt**：
```
实现 API 版本控制：
- URL 版本：/api/v1/users
- 支持多版本共存
- 版本迁移策略
```

---

## 项目四：实时聊天应用

### 项目概述

**目标**：创建一个实时聊天应用，支持私聊和群聊。

**技术栈**：
- 前端：React + Socket.io Client
- 后端：Node.js + Socket.io
- 数据库：MongoDB
- 消息队列：Redis

### 开发过程

#### 阶段 1：WebSocket 基础

**Prompt**：
```
创建 WebSocket 服务器：

功能：
- 用户连接/断开
- 发送消息
- 接收消息
- 在线用户列表

使用 Socket.io
```

#### 阶段 2：房间管理

**Prompt**：
```
实现聊天房间功能：

- 创建房间
- 加入房间
- 离开房间
- 房间消息
- 房间成员列表
```

#### 阶段 3：消息存储

**Prompt**：
```
实现消息存储：

- 保存消息到数据库
- 消息历史记录
- 未读消息计数
- 消息搜索
```

### 遇到的问题和解决方案

#### 问题 1：消息顺序

**问题**：多服务器时消息顺序混乱

**解决方案 Prompt**：
```
解决消息顺序问题：
- 使用消息 ID 和时间戳
- 客户端排序
- 服务器端验证
```

---

## 经验总结

### 成功的关键因素

1. **清晰的规划**：在开始前明确需求和架构
2. **迭代开发**：分阶段实现，逐步完善
3. **及时测试**：每个功能完成后立即测试
4. **代码审查**：即使 AI 生成，也要审查
5. **持续优化**：根据反馈不断改进

### 常见挑战

1. **需求理解偏差**：通过详细描述和示例减少
2. **性能问题**：及时发现和优化
3. **安全问题**：始终关注安全性
4. **代码质量**：保持高标准

### 最佳实践

1. **从简单开始**：先实现核心功能
2. **逐步扩展**：再添加高级功能
3. **保持测试**：始终编写测试
4. **文档完善**：记录开发过程
5. **持续学习**：从项目中学习

---

## 下一步

- 查看 [高级指南](./advanced-guide.md) 学习更多技巧
- 学习 [Prompt 工程](./prompt-engineering.md) 提高效率
- 阅读 [故障排除](./troubleshooting.md) 解决常见问题

---

**通过实践，不断进步！** 🚀
