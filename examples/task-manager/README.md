# Task Manager - 高级任务管理应用

> 使用 Vibe Coding 方法创建的现代化任务管理应用，包含数据库、Web 界面和丰富的功能

## 📖 项目介绍

这是一个功能完整的任务管理应用，展示了如何使用 Vibe Coding 方法开发一个包含数据库、后端 API 和前端界面的完整 Web 应用。项目使用 Flask 作为后端，SQLite 作为数据库，提供现代化的 Web 界面。

## 🎯 项目功能

### 核心功能
- ✅ 任务的创建、编辑、删除和完成
- ✅ 任务优先级设置（高、中、低）
- ✅ 任务分类和标签
- ✅ 截止日期设置
- ✅ 任务搜索和筛选
- ✅ 任务统计和仪表板
- ✅ 数据持久化存储

### 高级功能
- ✅ 任务排序（按优先级、日期、状态）
- ✅ 任务筛选（按状态、优先级、分类）
- ✅ 任务统计（总数、完成数、进行中）
- ✅ 响应式设计，支持移动端
- ✅ 数据导出功能

## 🏗️ 项目结构

```
task-manager/
├── README.md              # 项目说明
├── requirements.txt       # Python 依赖
├── app.py                 # Flask 后端主程序
├── models.py              # 数据模型
├── database.py            # 数据库操作
├── static/                # 静态资源
│   ├── css/
│   │   └── style.css      # 样式文件
│   └── js/
│       └── app.js         # 前端 JavaScript
├── templates/             # HTML 模板
│   ├── index.html         # 主界面
│   └── stats.html         # 统计页面
└── tasks.db               # SQLite 数据库（自动生成）
```

## 🚀 如何使用 Vibe Coding 创建这个项目

### 步骤 1: 项目初始化

在 Cursor 中：

1. 创建项目文件夹 `task-manager`
2. 按 `Cmd/Ctrl + I` 打开 AI 对话面板
3. 输入：
   ```
   我想创建一个任务管理应用，使用 Flask 和 SQLite。
   请帮我创建项目结构，包括：
   - app.py（Flask 主程序）
   - models.py（数据模型）
   - database.py（数据库操作）
   - requirements.txt（依赖文件）
   - templates/ 和 static/ 文件夹
   ```

### 步骤 2: 设计数据模型

```
请设计任务数据模型，包含以下字段：
- id（主键）
- title（标题）
- description（描述）
- priority（优先级：高、中、低）
- status（状态：待办、进行中、已完成）
- category（分类）
- due_date（截止日期）
- created_at（创建时间）
- updated_at（更新时间）
```

### 步骤 3: 实现后端 API

```
请实现以下 API 端点：
1. GET /api/tasks - 获取所有任务（支持筛选和排序）
2. GET /api/tasks/<id> - 获取单个任务
3. POST /api/tasks - 创建新任务
4. PUT /api/tasks/<id> - 更新任务
5. DELETE /api/tasks/<id> - 删除任务
6. GET /api/stats - 获取任务统计信息
```

### 步骤 4: 实现前端界面

```
请创建前端界面：
1. 主界面 - 显示任务列表，支持筛选、排序和搜索
2. 任务卡片 - 显示任务信息，支持快速操作
3. 任务表单 - 创建和编辑任务
4. 统计面板 - 显示任务统计信息
5. 使用现代化的 UI 设计，响应式布局
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

访问 `http://localhost:5000` 查看任务管理应用。

## 📝 API 文档

### 获取所有任务

```http
GET /api/tasks?status=进行中&priority=高&sort=due_date&order=asc
```

查询参数：
- `status`: 任务状态（待办、进行中、已完成）
- `priority`: 优先级（高、中、低）
- `category`: 分类
- `sort`: 排序字段（created_at, due_date, priority）
- `order`: 排序方向（asc, desc）
- `search`: 搜索关键词

### 获取单个任务

```http
GET /api/tasks/1
```

### 创建任务

```http
POST /api/tasks
Content-Type: application/json

{
  "title": "完成项目文档",
  "description": "编写项目 README 和 API 文档",
  "priority": "高",
  "category": "工作",
  "due_date": "2024-12-31"
}
```

### 更新任务

```http
PUT /api/tasks/1
Content-Type: application/json

{
  "status": "进行中",
  "priority": "中"
}
```

### 删除任务

```http
DELETE /api/tasks/1
```

### 获取统计信息

```http
GET /api/stats
```

响应：
```json
{
  "total": 50,
  "pending": 20,
  "in_progress": 15,
  "completed": 15,
  "by_priority": {
    "高": 10,
    "中": 25,
    "低": 15
  },
  "by_category": {...}
}
```

## 🎨 技术栈

- **后端**: Flask, SQLite
- **前端**: HTML5, CSS3, JavaScript (原生)
- **数据库**: SQLite
- **API**: RESTful API

## 📚 学习要点

通过这个项目，你学会了：

1. **数据模型设计**：如何设计合理的数据库结构
2. **复杂查询**：实现筛选、排序、搜索功能
3. **状态管理**：处理任务的不同状态和状态转换
4. **用户体验**：设计直观易用的界面
5. **数据统计**：实现数据分析和可视化

## 🔄 扩展功能建议

完成基础功能后，可以尝试添加：

- 用户认证和授权
- 任务协作（多人共享任务）
- 任务提醒和通知
- 任务附件上传
- 任务评论功能
- 任务模板
- 数据导入/导出（CSV、JSON）
- 任务看板视图（Kanban）
- 任务日历视图
- 任务依赖关系

## 💡 Vibe Coding 技巧

1. **分阶段实现**：先实现核心功能，再添加高级功能
2. **数据验证**：让 AI 添加完善的数据验证和错误处理
3. **用户体验**：关注界面交互，不断优化用户体验
4. **性能优化**：对于大量数据，考虑分页和索引优化
5. **代码组织**：保持代码结构清晰，便于维护和扩展

---

**祝你学习愉快！** 🚀

返回 [Vibe Coding 初学者指南](../../tutorials/vibe-coding/beginner-guide.md)
