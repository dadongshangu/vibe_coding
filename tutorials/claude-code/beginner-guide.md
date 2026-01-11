# Claude Code 入门指南

> 从零开始学习 Claude Code CLI 工具

## 📖 目录

1. [什么是 Claude Code](#什么是-claude-code)
2. [为什么选择 Claude Code](#为什么选择-claude-code)
3. [安装与配置](#安装与配置)
4. [基础使用](#基础使用)
5. [核心功能介绍](#核心功能介绍)
6. [与 Cursor 的对比](#与-cursor-的对比)
7. [常见问题解答](#常见问题解答)
8. [实用工作流程](#实用工作流程)
9. [最佳实践](#最佳实践)

---

## 什么是 Claude Code

### 概念解释

**Claude Code** 是 Anthropic 公司开发的命令行 AI 编程助手工具，基于 Claude 模型，专门为开发者设计。它通过命令行界面与 AI 交互，帮助开发者更高效地编写代码、调试程序和管理项目。

### 核心特点

1. **命令行工具**：直接在终端中使用，无需打开额外的编辑器
2. **上下文感知**：能够理解整个项目的结构和代码库
3. **Git 集成**：与 Git 工作流程深度集成，简化版本控制
4. **项目配置**：通过 `CLAUDE.md` 文件管理项目上下文
5. **多语言支持**：支持多种编程语言和框架

### 适用场景

- **快速原型开发**：快速生成代码原型和示例
- **代码重构**：帮助重构和优化现有代码
- **问题调试**：分析错误和提供解决方案
- **文档生成**：自动生成代码文档和注释
- **Git 操作**：自动生成提交信息、创建分支等

---

## 为什么选择 Claude Code

### 优势

1. **轻量级**：不需要安装大型 IDE，只需命令行工具
2. **快速响应**：直接在终端中交互，无需切换窗口
3. **项目感知**：能够理解整个项目的上下文
4. **Git 友好**：深度集成 Git，简化版本控制流程
5. **灵活配置**：通过配置文件自定义行为

### 与 Cursor 的互补

- **Cursor**：适合在 IDE 中实时编辑和开发
- **Claude Code**：适合快速任务、批量操作和命令行工作流

两者可以配合使用，在不同场景下发挥各自优势。

---

## 安装与配置

### 系统要求

- **Node.js**：版本 18 或更高
- **操作系统**：macOS、Linux 或 Windows
- **网络连接**：需要访问 Anthropic API

### 安装方法

#### 方法 1：NPM 全局安装（推荐）

```bash
npm install -g @anthropic-ai/claude-code
```

#### 方法 2：原生安装

**macOS 和 Linux：**

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows PowerShell：**

```powershell
irm https://claude.ai/install.ps1 | iex
```

**Windows CMD：**

```cmd
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

### 验证安装

安装完成后，在终端中运行：

```bash
claude --version
```

如果显示版本号，说明安装成功。

### 首次配置

1. **获取 API Key**

   - 访问 [Anthropic 官网](https://www.anthropic.com/)
   - 注册账号并获取 API Key
   - 将 API Key 保存到安全位置

2. **设置环境变量**

   **macOS/Linux：**

   ```bash
   export ANTHROPIC_API_KEY="your-api-key-here"
   ```

   或者添加到 `~/.bashrc` 或 `~/.zshrc`：

   ```bash
   echo 'export ANTHROPIC_API_KEY="your-api-key-here"' >> ~/.bashrc
   source ~/.bashrc
   ```

   **Windows PowerShell：**

   ```powershell
   $env:ANTHROPIC_API_KEY="your-api-key-here"
   ```

   或者添加到系统环境变量中。

3. **初始化项目（可选）**

   在项目根目录运行：

   ```bash
   claude init
   ```

   这会创建一个 `CLAUDE.md` 文件，用于配置项目上下文。

---

## 基础使用

### 启动 Claude Code

在终端中直接输入：

```bash
claude
```

这会启动交互式会话，你可以直接与 Claude 对话。

### 基本命令

#### 查看帮助

```bash
claude --help
```

或在使用过程中输入：

```
/help
```

#### 清除上下文

```
/clear
```

清除当前会话的上下文，开始新的对话。

#### 退出

```
/exit
```

或按 `Ctrl+C` 退出。

### 交互方式

#### 1. 直接提问

```
如何创建一个 React 组件？
```

#### 2. 请求代码生成

```
帮我写一个 Python 函数，计算斐波那契数列的第 n 项
```

#### 3. 代码审查

```
请审查这段代码，找出潜在问题：
[粘贴代码]
```

#### 4. 文件操作

```
分析当前目录下的 main.py 文件
```

---

## 核心功能介绍

### 1. 代码生成

Claude Code 可以根据你的描述生成代码：

**示例：**

```
创建一个 Flask 应用，包含用户注册和登录功能
```

Claude Code 会生成完整的代码结构，包括路由、数据库模型等。

### 2. 代码解释

不理解某段代码？让 Claude Code 解释：

```
解释这段代码的作用：
[粘贴代码]
```

### 3. 代码重构

帮助优化和重构代码：

```
重构这段代码，提高可读性和性能：
[粘贴代码]
```

### 4. 错误调试

遇到错误？让 Claude Code 帮你分析：

```
这段代码报错了，请帮我找出问题：
[粘贴代码和错误信息]
```

### 5. Git 集成

#### 生成提交信息

```bash
claude commit
```

Claude Code 会分析你的更改，自动生成合适的提交信息。

#### 创建分支

```bash
claude branch feature/new-feature
```

#### 查看差异

```bash
claude diff
```

### 6. 项目初始化

```bash
claude init
```

创建 `CLAUDE.md` 文件，配置项目上下文。

### 7. 文档生成

```
为这个函数生成文档字符串：
[粘贴函数代码]
```

---

## 与 Cursor 的对比

### 功能对比

| 特性 | Claude Code | Cursor |
|------|------------|--------|
| **使用方式** | 命令行工具 | IDE 编辑器 |
| **实时编辑** | ❌ | ✅ |
| **代码补全** | ❌ | ✅ |
| **多文件编辑** | ✅ | ✅ |
| **Git 集成** | ✅ 深度集成 | ✅ 基础集成 |
| **项目上下文** | ✅ CLAUDE.md | ✅ 代码库索引 |
| **学习曲线** | 低 | 中 |
| **适用场景** | 快速任务、批量操作 | 日常开发、实时编辑 |

### 使用建议

- **使用 Claude Code**：
  - 快速生成代码原型
  - 批量处理文件
  - Git 操作自动化
  - 命令行工作流

- **使用 Cursor**：
  - 日常代码编辑
  - 实时代码补全
  - 多文件协同编辑
  - IDE 集成开发

### 配合使用

两者可以完美配合：

1. 用 **Claude Code** 快速生成项目骨架
2. 用 **Cursor** 进行详细开发和调试
3. 用 **Claude Code** 进行批量重构和优化
4. 用 **Cursor** 进行最终测试和部署

---

## 常见问题解答

### Q1: Claude Code 和 Cursor 有什么区别？

**A:** Claude Code 是命令行工具，适合快速任务和自动化；Cursor 是 IDE，适合日常开发。两者可以配合使用。

### Q2: 需要付费吗？

**A:** Claude Code 本身是免费的，但使用 Anthropic API 可能需要付费（取决于使用量）。建议查看 Anthropic 的定价页面。

### Q3: 支持哪些编程语言？

**A:** Claude Code 支持主流编程语言，包括 Python、JavaScript、TypeScript、Java、Go、Rust 等。

### Q4: 如何提高代码生成质量？

**A:** 
- 提供清晰的上下文
- 使用 `CLAUDE.md` 配置项目信息
- 给出具体的示例和要求
- 逐步迭代，不要一次性要求太多

### Q5: 生成的代码可以直接使用吗？

**A:** 建议审查和测试生成的代码。虽然 Claude Code 很强大，但生成的代码可能需要根据你的具体需求进行调整。

### Q6: 如何处理大型项目？

**A:** 
- 使用 `CLAUDE.md` 文件提供项目概览
- 分模块处理，不要一次性处理整个项目
- 使用 Git 集成功能管理更改

### Q7: 可以离线使用吗？

**A:** 不可以。Claude Code 需要网络连接来访问 Anthropic API。

### Q8: 如何保护 API Key？

**A:** 
- 使用环境变量存储 API Key
- 不要将 API Key 提交到 Git 仓库
- 定期轮换 API Key
- 使用 `.gitignore` 忽略包含 API Key 的文件

---

## 实用工作流程

### 工作流程 1：快速原型开发

1. **初始化项目**

   ```bash
   mkdir my-project
   cd my-project
   claude init
   ```

2. **描述需求**

   ```
   创建一个待办事项应用，使用 Flask 后端和 React 前端
   ```

3. **生成代码**

   Claude Code 会生成项目结构和初始代码。

4. **迭代优化**

   ```
   添加用户认证功能
   ```

### 工作流程 2：代码重构

1. **分析现有代码**

   ```
   分析这个文件，找出可以优化的地方：
   [文件路径]
   ```

2. **生成重构方案**

   Claude Code 会提供重构建议。

3. **应用更改**

   使用 Git 集成功能管理更改：

   ```bash
   claude commit
   ```

### 工作流程 3：错误调试

1. **描述问题**

   ```
   这个函数报错了，错误信息是：
   [错误信息]
   代码是：
   [代码]
   ```

2. **获取解决方案**

   Claude Code 会分析问题并提供修复建议。

3. **验证修复**

   测试修复后的代码。

### 工作流程 4：文档生成

1. **选择文件或函数**

   ```
   为 src/utils/helpers.py 中的所有函数生成文档字符串
   ```

2. **生成文档**

   Claude Code 会生成符合规范的文档字符串。

3. **应用到代码**

   将生成的文档添加到代码中。

---

## 最佳实践

### 1. 使用 CLAUDE.md 文件

在项目根目录创建 `CLAUDE.md`，包含：

```markdown
# 项目名称

## 技术栈
- 前端：React 18
- 后端：Node.js 18
- 数据库：PostgreSQL

## 编码规范
- 使用 ESLint
- 遵循 Airbnb 风格指南
- 使用 TypeScript

## 项目结构
- src/ - 源代码
- tests/ - 测试文件
- docs/ - 文档

## 特殊要求
- 所有 API 需要认证
- 使用 JWT 令牌
```

### 2. 提供清晰的上下文

在提问时，提供足够的上下文信息：

**不好的提问：**
```
写一个函数
```

**好的提问：**
```
写一个 Python 函数，接收用户 ID 列表，返回这些用户的详细信息。
使用 SQLAlchemy ORM，从 users 表中查询。
如果用户不存在，返回 None。
```

### 3. 分步骤迭代

不要一次性要求太多功能，分步骤进行：

1. 先实现核心功能
2. 再添加辅助功能
3. 最后优化和测试

### 4. 审查生成的代码

始终审查 Claude Code 生成的代码：
- 检查逻辑是否正确
- 验证是否符合项目规范
- 运行测试确保功能正常

### 5. 使用 Git 集成

充分利用 Git 集成功能：
- 使用 `claude commit` 生成提交信息
- 使用 `claude diff` 查看更改
- 使用分支管理功能

### 6. 保存有用的提示

将有效的提示保存下来，形成模板库，提高效率。

### 7. 定期更新

保持 Claude Code 和依赖项的最新版本：

```bash
npm update -g @anthropic-ai/claude-code
```

---

## 下一步学习

完成入门指南后，建议继续学习：

- [Claude Code 高级技巧](../claude-code/advanced-techniques.md) - 深入学习高级功能
- [Prompt 工程完全指南](../vibe-coding/prompt-engineering.md) - 掌握提示工程技巧
- [Vibe Coding 高级指南](../vibe-coding/advanced-guide.md) - 学习高级开发技巧

---

<div style="display: flex; justify-content: space-between; align-items: center; margin: 40px 0; padding: 20px; background: #f5f5f5; border-radius: 8px; flex-wrap: wrap;">
  <div style="flex: 1; min-width: 150px;">
    <p style="margin: 0; color: #666; font-size: 14px;">上一篇</p>
    <p style="margin: 5px 0 0 0;">
      <a href="/vibe_coding/tutorials/cursor/quick-reference.html" style="color: #0366d6; text-decoration: none; font-weight: 500;">← Cursor 快速参考手册</a>
    </p>
  </div>
  <div style="flex: 1; text-align: center; min-width: 150px;">
    <p style="margin: 0;">
      <a href="/vibe_coding/" style="color: #0366d6; text-decoration: none; font-weight: 500;">🏠 返回主页</a>
    </p>
  </div>
  <div style="flex: 1; text-align: right; min-width: 150px;">
    <p style="margin: 0; color: #666; font-size: 14px;">下一篇</p>
    <p style="margin: 5px 0 0 0;">
      <a href="/vibe_coding/tutorials/vibe-coding/prompt-engineering.html" style="color: #0366d6; text-decoration: none; font-weight: 500;">Prompt 工程完全指南 →</a>
    </p>
  </div>
</div>

---

**祝你学习愉快！** 🚀
