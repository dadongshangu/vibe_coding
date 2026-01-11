# Cursor 快速参考手册

> Cursor IDE 快捷键、命令和配置速查表

## 📋 目录

1. [快捷键速查表](#快捷键速查表)
2. [常用命令](#常用命令)
3. [界面布局说明](#界面布局说明)
4. [配置建议](#配置建议)
5. [AI 功能使用](#ai-功能使用)

---

## 快捷键速查表

### AI 相关快捷键

| 快捷键 | 功能 | 说明 |
|--------|------|------|
| `Tab` | 接受代码补全 | 当看到灰色提示时按 Tab 接受 |
| `Esc` | 拒绝代码补全 | 拒绝当前的 AI 建议 |
| `Cmd/Ctrl + K` | 内联编辑 | 选中代码后按此键，输入修改指令 |
| `Cmd/Ctrl + I` | 打开 AI 对话面板 | 与 AI 对话，提问、生成代码 |
| `Cmd/Ctrl + L` | 打开 Composer | Cursor 2.0 的新功能，多文件编辑 |

### 编辑快捷键

| 快捷键 | 功能 | 说明 |
|--------|------|------|
| `Cmd/Ctrl + /` | 注释/取消注释 | 切换当前行的注释状态 |
| `Alt + Click` | 多光标 | 在多个位置创建光标 |
| `Cmd/Ctrl + D` | 选中下一个相同文本 | 快速选中所有相同文本 |
| `Cmd/Ctrl + Shift + K` | 删除整行 | 删除当前行 |
| `Alt + ↑/↓` | 移动行 | 向上或向下移动当前行 |
| `Shift + Alt + ↑/↓` | 复制行 | 向上或向下复制当前行 |
| `Cmd/Ctrl + Enter` | 在下方插入新行 | 在当前行下方插入新行 |
| `Cmd/Ctrl + Shift + Enter` | 在上方插入新行 | 在当前行上方插入新行 |

### 导航快捷键

| 快捷键 | 功能 | 说明 |
|--------|------|------|
| `Cmd/Ctrl + P` | 快速打开文件 | 输入文件名快速打开 |
| `Cmd/Ctrl + Shift + P` | 命令面板 | 打开命令面板，执行各种命令 |
| `Cmd/Ctrl + B` | 切换侧边栏 | 显示/隐藏左侧边栏 |
| `Cmd/Ctrl + J` | 切换面板 | 显示/隐藏底部面板 |
| `Cmd/Ctrl + \` | 分屏 | 将编辑器分成多个窗格 |
| `Cmd/Ctrl + 1/2/3` | 切换编辑器组 | 在多个编辑器组之间切换 |
| `Cmd/Ctrl + W` | 关闭当前标签 | 关闭当前打开的文件 |
| `Cmd/Ctrl + K W` | 关闭所有标签 | 关闭所有打开的文件 |

### 搜索快捷键

| 快捷键 | 功能 | 说明 |
|--------|------|------|
| `Cmd/Ctrl + F` | 在当前文件搜索 | 在当前文件中搜索文本 |
| `Cmd/Ctrl + H` | 在当前文件替换 | 在当前文件中查找并替换 |
| `Cmd/Ctrl + Shift + F` | 全局搜索 | 在整个项目中搜索 |
| `Cmd/Ctrl + Shift + H` | 全局替换 | 在整个项目中查找并替换 |
| `Cmd/Ctrl + G` | 查找下一个 | 查找下一个匹配项 |
| `Shift + Cmd/Ctrl + G` | 查找上一个 | 查找上一个匹配项 |

### Git 快捷键

| 快捷键 | 功能 | 说明 |
|--------|------|------|
| `Cmd/Ctrl + Shift + G` | 打开源代码管理 | 打开 Git 面板 |
| `Cmd/Ctrl + Enter` | 提交更改 | 在源代码管理面板中，输入提交信息后按此键提交 |

### 调试快捷键

| 快捷键 | 功能 | 说明 |
|--------|------|------|
| `F5` | 开始调试 | 启动调试会话 |
| `F9` | 切换断点 | 在当前行设置/取消断点 |
| `F10` | 单步跳过 | 执行下一行，不进入函数 |
| `F11` | 单步进入 | 进入函数内部 |
| `Shift + F11` | 单步跳出 | 跳出当前函数 |
| `Shift + F5` | 停止调试 | 停止调试会话 |

---

## 常用命令

### 命令面板常用命令

按 `Cmd/Ctrl + Shift + P` 打开命令面板，输入以下命令：

#### 文件操作

- `File: New File` - 创建新文件
- `File: New Folder` - 创建新文件夹
- `File: Save` - 保存文件
- `File: Save All` - 保存所有文件
- `File: Revert File` - 撤销文件更改

#### 编辑操作

- `Editor: Format Document` - 格式化整个文档
- `Editor: Format Selection` - 格式化选中部分
- `Editor: Indent Lines` - 增加缩进
- `Editor: Outdent Lines` - 减少缩进
- `Editor: Toggle Word Wrap` - 切换自动换行

#### 视图操作

- `View: Toggle Primary Side Bar` - 切换主侧边栏
- `View: Toggle Terminal` - 切换终端
- `View: Toggle Problems` - 切换问题面板
- `View: Zoom In` - 放大
- `View: Zoom Out` - 缩小
- `View: Reset Zoom` - 重置缩放

#### AI 相关命令

- `Cursor: Open Chat` - 打开 AI 对话面板
- `Cursor: Open Composer` - 打开 Composer（Cursor 2.0）
- `Cursor: Accept Inline Suggestion` - 接受内联建议
- `Cursor: Reject Inline Suggestion` - 拒绝内联建议

#### Git 命令

- `Git: Clone` - 克隆仓库
- `Git: Commit` - 提交更改
- `Git: Push` - 推送到远程
- `Git: Pull` - 从远程拉取
- `Git: Show Output` - 显示 Git 输出

---

## 界面布局说明

### 主要区域

```
┌─────────────────────────────────────────────────────────┐
│  菜单栏 (Menu Bar)                                       │
├──────┬───────────────────────────────────┬──────────────┤
│      │                                   │              │
│ 侧边 │        编辑器区域                 │   AI 面板    │
│ 栏   │      (Editor Area)                │  (AI Panel)  │
│      │                                   │              │
│      │                                   │              │
├──────┴───────────────────────────────────┴──────────────┤
│  状态栏 (Status Bar)                                      │
├──────────────────────────────────────────────────────────┤
│  面板 (Panel) - 终端、问题、输出等                        │
└──────────────────────────────────────────────────────────┘
```

### 侧边栏图标说明

| 图标 | 功能 | 快捷键 |
|------|------|--------|
| 📁 | 资源管理器 | `Cmd/Ctrl + Shift + E` |
| 🔍 | 搜索 | `Cmd/Ctrl + Shift + F` |
| 🌿 | 源代码管理 (Git) | `Cmd/Ctrl + Shift + G` |
| 🐛 | 运行和调试 | `Cmd/Ctrl + Shift + D` |
| 📦 | 扩展 | `Cmd/Ctrl + Shift + X` |

### 状态栏说明

状态栏显示的信息：

- **分支名称**：当前 Git 分支
- **错误/警告数量**：代码中的问题数量
- **语言模式**：当前文件的编程语言
- **编码格式**：文件编码（如 UTF-8）
- **行尾符**：LF 或 CRLF
- **缩进**：空格数或 Tab

---

## 配置建议

### 推荐设置

打开设置：`Cmd/Ctrl + ,`

#### 编辑器设置

```json
{
  // 字体大小
  "editor.fontSize": 14,
  
  // 自动保存
  "files.autoSave": "afterDelay",
  "files.autoSaveDelay": 1000,
  
  // 自动格式化
  "editor.formatOnSave": true,
  "editor.formatOnPaste": true,
  
  // 代码补全
  "editor.suggestSelection": "first",
  "editor.wordBasedSuggestions": "allDocuments",
  
  // 缩进
  "editor.tabSize": 2,
  "editor.insertSpaces": true,
  
  // 行号
  "editor.lineNumbers": "on",
  "editor.rulers": [80, 120],
  
  // 自动换行
  "editor.wordWrap": "on"
}
```

#### AI 设置

```json
{
  // AI 补全延迟（毫秒）
  "cursor.cpp.disabledLanguages": [],
  
  // 内联建议
  "editor.inlineSuggest.enabled": true,
  
  // 接受建议的快捷键
  "editor.acceptSuggestionOnCommitCharacter": true
}
```

#### 文件设置

```json
{
  // 排除文件
  "files.exclude": {
    "**/.git": true,
    "**/.DS_Store": true,
    "**/node_modules": true
  },
  
  // 文件关联
  "files.associations": {
    "*.md": "markdown"
  }
}
```

### 推荐扩展

虽然 Cursor 已经集成了 AI 功能，但以下扩展仍然有用：

- **GitLens** - 增强 Git 功能
- **Prettier** - 代码格式化
- **ESLint** - JavaScript/TypeScript 代码检查
- **Python** - Python 语言支持
- **Docker** - Docker 文件支持

---

## AI 功能使用

### 代码补全

1. **自动触发**：开始输入代码时自动出现
2. **接受建议**：按 `Tab` 键
3. **拒绝建议**：按 `Esc` 键或继续输入
4. **查看多个建议**：使用 `Ctrl + →` 或 `Ctrl + ←` 切换

### 内联编辑 (Cmd/Ctrl + K)

**使用步骤**：

1. 选中要修改的代码
2. 按 `Cmd/Ctrl + K`
3. 输入修改指令
4. 按 `Enter` 执行

**示例指令**：
- "将这个函数改为异步函数"
- "添加错误处理"
- "优化这段代码的性能"
- "添加类型注解"

### AI 对话面板 (Cmd/Ctrl + I)

**使用场景**：

1. **提问**：
   - "解释这段代码的作用"
   - "这段代码有什么问题？"

2. **生成代码**：
   - "写一个函数来计算斐波那契数列"
   - "创建一个用户登录的 API 端点"

3. **重构代码**：
   - "重构这个类，使其更符合 SOLID 原则"
   - "将这个函数拆分成更小的函数"

4. **调试**：
   - "为什么这段代码会报错？"
   - "如何修复这个 bug？"

**技巧**：

- 选中代码后再提问，提供上下文
- 描述要具体清晰
- 可以连续对话，基于之前的回答继续提问

### Composer (Cursor 2.0)

**功能**：多文件编辑和项目级别的代码生成

**使用方法**：

1. 按 `Cmd/Ctrl + L` 打开 Composer
2. 描述你想要实现的功能
3. Cursor 会分析整个项目并生成/修改多个文件
4. 审查更改后接受或拒绝

**适用场景**：

- 创建新功能模块
- 大型重构
- 添加测试
- 实现设计模式

---

## 实用技巧

### 1. 多光标编辑

- **Alt + Click**：在多个位置创建光标
- **Cmd/Ctrl + Alt + ↑/↓**：在上方/下方创建光标
- **Cmd/Ctrl + D**：选中下一个相同文本（可多次按）
- **Cmd/Ctrl + Shift + L**：选中所有相同文本

### 2. 快速导航

- **Cmd/Ctrl + P**：快速打开文件
- **Cmd/Ctrl + Shift + O**：在当前文件中跳转到符号（函数、类等）
- **Cmd/Ctrl + T**：在整个项目中搜索符号
- **Cmd/Ctrl + G**：跳转到指定行号

### 3. 代码折叠

- **Cmd/Ctrl + Shift + [**：折叠当前区域
- **Cmd/Ctrl + Shift + ]**：展开当前区域
- **Cmd/Ctrl + K Cmd/Ctrl + 0**：折叠所有区域
- **Cmd/Ctrl + K Cmd/Ctrl + J**：展开所有区域

### 4. 分屏编辑

- **Cmd/Ctrl + \**：垂直分屏
- **Cmd/Ctrl + K Cmd/Ctrl + \**：水平分屏
- **Cmd/Ctrl + 1/2/3**：切换到不同的编辑器组
- **Cmd/Ctrl + K Cmd/Ctrl + W**：关闭所有编辑器组

---

## 故障排除

### 常见问题

#### AI 补全不工作

1. 检查是否登录 Cursor 账户
2. 检查网络连接
3. 检查 AI 配额是否用完
4. 重启 Cursor

#### 快捷键冲突

1. 打开设置：`Cmd/Ctrl + ,`
2. 搜索 "keyboard shortcuts"
3. 自定义冲突的快捷键

#### 代码格式化不工作

1. 安装相应的格式化扩展（如 Prettier）
2. 检查 `editor.formatOnSave` 设置
3. 手动格式化：`Cmd/Ctrl + Shift + P` → "Format Document"

---

## 总结

这份快速参考手册涵盖了 Cursor 最常用的功能和快捷键。建议：

1. **打印或保存**：将常用快捷键保存下来
2. **逐步学习**：不要试图记住所有快捷键，先掌握最常用的
3. **自定义**：根据个人习惯调整快捷键和设置
4. **实践**：多使用才能熟练掌握

---

**提示**：记住最常用的几个快捷键就能大大提高效率：
- `Tab` - 接受代码补全
- `Cmd/Ctrl + K` - 内联编辑
- `Cmd/Ctrl + I` - AI 对话
- `Cmd/Ctrl + P` - 快速打开文件

---

---

<div class="navigation">

<div class="nav-item">
  <p class="nav-label">上一篇</p>
  <p class="nav-link">
    <a href="../vibe-coding/beginner-guide.html">← Vibe Coding 初学者完全指南</a>
  </p>
</div>

<div class="nav-item center">
  <p class="nav-link">
    <a href="../../index.html">🏠 返回主页</a>
  </p>
</div>

<div class="nav-item right">
  <p class="nav-label">下一篇</p>
  <p class="nav-link">
    <a href="../vibe-coding/prompt-engineering.html">Prompt 工程完全指南 →</a>
  </p>
</div>

</div>

---

返回 [Vibe Coding 初学者指南](../vibe-coding/beginner-guide.html)
