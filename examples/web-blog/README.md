# Web Blog 项目示例

> 一个完整的个人博客系统，展示如何使用 Vibe Coding 开发真实项目

## 项目概述

这是一个功能完整的个人博客系统，包含文章管理、用户系统、评论功能等。

## 功能特性

- ✅ 文章 CRUD（创建、读取、更新、删除）
- ✅ Markdown 支持
- ✅ 文章分类和标签
- ✅ 用户认证（注册、登录）
- ✅ 评论系统
- ✅ 搜索功能
- ✅ 响应式设计
- ✅ SEO 优化

## 技术栈

- **后端**：Node.js + Express + MongoDB
- **前端**：React + Next.js
- **样式**：Tailwind CSS
- **部署**：Vercel

## 如何使用 Vibe Coding 开发

### 步骤 1：项目初始化

在 Cursor 中打开 AI 对话（`Cmd/Ctrl + I`）：

```
创建一个博客系统项目：
- 使用 Next.js 框架
- 使用 TypeScript
- 配置 Tailwind CSS
- 创建基础项目结构
```

### 步骤 2：数据模型设计

```
设计博客系统的数据模型：

1. User 模型
   - id, email, password, name, role, createdAt

2. Article 模型
   - id, title, content, author, category, tags, status, createdAt, updatedAt

3. Category 模型
   - id, name, description

使用 MongoDB + Mongoose
```

### 步骤 3：后端 API 开发

```
创建文章管理的 REST API：

GET    /api/articles        # 获取文章列表
GET    /api/articles/:id    # 获取单篇文章
POST   /api/articles        # 创建文章（需要认证）
PUT    /api/articles/:id    # 更新文章（需要认证）
DELETE /api/articles/:id    # 删除文章（需要认证）

要求：
- 使用 JWT 认证
- 输入验证
- 错误处理
```

### 步骤 4：前端页面开发

```
创建博客前端页面：

1. 首页（文章列表）
   - 显示最新文章
   - 分页
   - 分类筛选

2. 文章详情页
   - 显示文章内容（Markdown 渲染）
   - 相关文章推荐

3. 管理后台
   - 文章列表
   - 创建/编辑文章
```

### 步骤 5：功能完善

```
添加评论系统：
- 用户可以评论文章
- 支持回复评论
- 评论审核（管理员）
```

## 项目结构

```
web-blog/
├── backend/
│   ├── models/      # 数据模型
│   ├── routes/      # 路由
│   ├── controllers/ # 控制器
│   └── middleware/  # 中间件
├── frontend/
│   ├── components/  # 组件
│   ├── pages/       # 页面
│   └── styles/     # 样式
└── shared/          # 共享代码
```

## 学习要点

通过这个项目，你将学习：

1. **项目规划**：如何规划一个完整项目
2. **架构设计**：前后端分离架构
3. **API 设计**：RESTful API 设计
4. **数据建模**：数据库设计
5. **用户认证**：JWT 认证实现
6. **Markdown 处理**：Markdown 渲染
7. **SEO 优化**：搜索引擎优化

## 扩展功能

完成基础功能后，可以添加：

- 文章搜索
- 标签云
- 文章统计
- 访问量统计
- RSS 订阅
- 邮件通知

## 参考

- 查看 [实战案例](../../tutorials/vibe-coding/case-studies.md) 了解完整开发过程
- 学习 [高级指南](../../tutorials/vibe-coding/advanced-guide.md) 掌握更多技巧

---

**开始你的博客项目吧！** 🚀
