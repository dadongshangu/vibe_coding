# Cursor CLI 安装与使用指南

> 在终端中直接使用 Cursor AI Agent，支持交互式对话与脚本自动化

## 📋 目录

1. [简介](#简介)
2. [安装](#安装)
3. [验证安装](#验证安装)
4. [交互式模式](#交互式模式)
5. [非交互式模式（脚本/无头）](#非交互式模式脚本无头)
6. [工作模式](#工作模式)
7. [会话管理](#会话管理)
8. [Cloud Agent 交接](#cloud-agent-交接)
9. [常用场景示例](#常用场景示例)
10. [故障排除](#故障排除)

---

## 简介

**Cursor CLI** 让你在终端里直接与 AI Agent 交互，用于编写、审查和修改代码。无论你喜欢在终端里对话，还是在脚本或 CI 里用“打印模式”自动化，CLI 都能在命令行里提供同样的能力。

- **交互式**：像和助手聊天一样描述目标、审查修改、批准命令
- **无头/脚本**：用 `-p` / `--print` 做非交互式任务（代码审查、安全扫描、批量处理等）
- **多模型**：支持 Anthropic、OpenAI、Gemini 等前沿模型
- **环境无关**：可在任意 IDE 或终端使用（VS Code、JetBrains、Neovim 等）

> **注意**：使用 Cursor CLI 需要有效的 Cursor 订阅；首次使用可能需登录 Cursor 账户完成认证。

---

## 安装

### Windows（PowerShell）

在 **PowerShell** 中执行（建议以管理员身份运行，以便写入 PATH）：

```powershell
irm 'https://cursor.com/install?win32=true' | iex
```

安装完成后，**重新打开终端**（或新开一个 PowerShell 窗口），再使用 `agent` 命令。

### macOS / Linux / WSL

```bash
curl https://cursor.com/install -fsS | bash
```

安装后若找不到 `agent`，可重启终端或执行 `source ~/.bashrc` / `source ~/.zshrc`。

---

## 验证安装

在终端中运行：

```bash
agent --version
```

若输出版本号（例如 `2026.01.28-fd13201`），说明安装成功。也可用 `agent -h` 或 `agent --help` 查看帮助。

---

## 交互式模式

在终端里和 Agent 对话，描述目标、查看建议、决定是否执行。

### 启动交互会话

```bash
# 直接启动，进入对话
agent

# 带初始提示启动
agent "把 auth 模块重构为使用 JWT"
agent "给这个项目加单元测试"
```

进入后可以连续输入多轮指令，Agent 会读文件、改代码、运行命令（经你确认），和 Cursor 编辑器里的 Agent 行为一致。

### 交互中的常用操作

- **发送任务**：输入自然语言描述，回车
- **审查修改**：Agent 会列出将要改动的文件与内容，按提示接受/拒绝
- **切换模式**：可用 `/plan`、`/ask` 等（见下方 [工作模式](#工作模式)）
- **退出**：输入 `exit` 或按 `Ctrl+C`

---

## 非交互式模式（脚本/无头）

适合脚本、CI、自动化流水线：只输出结果，不等待人工确认。

### 基本用法

使用 **打印模式**：`-p` 或 `--print`。

```bash
# 只分析/回答，不改文件
agent -p "这个项目是做什么的？"
agent -p "找出并说明性能问题"

# 指定模型（若你的账户支持）
agent -p "做一次安全审查" --model "gpt-5.2"
```

### 在脚本中允许改文件

在打印模式下，**默认不会写文件**。若要在脚本里真正改代码，需加上 `--force`：

```bash
# 允许 Agent 直接修改文件（无确认）
agent -p --force "把这段代码改成现代 ES6+ 语法"

# 不写 --force 时，只会给出建议，不落盘
agent -p "给这个文件加 JSDoc 注释"
```

### 输出格式

便于和脚本配合：

```bash
# 纯文本（默认），只要最终回答
agent -p "总结最近改动" --output-format text

# 结构化 JSON
agent -p "做代码审查并输出结构化结果" --output-format json

# 流式 JSON，适合实时进度
agent -p --output-format stream-json --stream-partial-output "分析项目并生成报告"
```

---

## 工作模式

CLI 与编辑器中的 Agent 模式一致，可切换：

| 模式   | 说明                     | 快捷方式 / 命令        |
|--------|--------------------------|-------------------------|
| Agent  | 完整能力，可读改代码、跑命令 | 默认                    |
| Plan   | 先规划再动手，多轮澄清   | `Shift+Tab`、`/plan`、`--mode=plan` |
| Ask    | 只读不写，仅探索与回答   | `/ask`、`--mode=ask`    |

示例：

```bash
# 以“只读”模式询问
agent --mode=ask "这段代码有没有内存泄漏风险？"

# 先规划再执行
agent --mode=plan "重构用户认证模块"
```

---

## 会话管理

可以恢复之前的对话，保持上下文。

```bash
# 列出历史会话
agent ls

# 恢复最近一次会话
agent resume

# 恢复指定会话（用 chat-id）
agent --resume="chat-id-here"
```

---

## Cloud Agent 交接

把当前对话“交给” [Cloud Agent](https://cursor.com/docs/cloud-agent)，在后台继续跑，你可以在 [cursor.com/agents](https://cursor.com/agents) 用网页或手机查看。

在**任意一条消息前加 `&`** 即可：

```text
& 把 auth 模块重构好并加上完整测试
```

---

## 常用场景示例

### 1. 快速问答（不改文件）

```bash
agent -p "这个代码库的主要功能是什么？"
agent -p "解释 src/auth.js 里的登录逻辑"
```

### 2. 代码审查（可写文件）

```bash
# 只输出审查意见
agent -p "对最近改动做代码审查，写进 review.txt" --output-format text

# 允许直接改代码
agent -p --force "按审查意见修复 src/utils.js"
```

### 3. 批量处理（脚本 + --force）

```bash
# 示例：给一批 JS 文件加 JSDoc（需根据实际路径调整）
Get-ChildItem -Path src -Filter "*.js" -Recurse | ForEach-Object {
  agent -p --force "为 $($_.FullName) 添加完整的 JSDoc 注释"
}
```

### 4. 图片/媒体分析

在提示里写上文件路径，Agent 会通过工具读取并分析：

```bash
agent -p "分析这张图并描述内容：./screenshot.png"
agent -p "对比这两张图：./before.png ./after.png"
```

### 5. 与 Git 结合

```bash
# 审查未提交的改动
agent -p "审查当前 git 改动，关注安全和可读性"
```

---

## 故障排除

### 找不到 `agent` 命令

- **Windows**：安装后请**新开一个 PowerShell 窗口**，或检查 PATH 是否包含 Cursor CLI 所在目录
- **macOS/Linux**：执行 `source ~/.bashrc` 或 `source ~/.zshrc`，或重新打开终端

### 认证失败 / 未登录

- 确保已安装并登录过 **Cursor 桌面应用**
- CLI 会复用 Cursor 的登录状态；若在无图形界面的环境（如 CI），需按官方文档配置 `CURSOR_API_KEY` 等（见 [Cursor 文档 - 认证](https://cursor.com/docs/cli/reference/authentication)）

### 脚本里加了 `-p --force` 但没改文件

- 确认提示语里明确说了要“修改/写入/重写”等
- 确认路径和文件权限正确，Agent 有权限写目标文件

### 更多帮助

- 命令帮助：`agent -h` / `agent --help`
- 官方文档：[Cursor CLI 概述](https://cursor.com/docs/cli/overview)、[无头模式](https://cursor.com/docs/cli/headless)

---

## 总结

| 需求           | 推荐用法 |
|----------------|----------|
| 终端里对话、改代码 | `agent` 或 `agent "任务描述"` |
| 脚本里只读/分析   | `agent -p "问题"` |
| 脚本里自动改文件  | `agent -p --force "任务"` |
| 指定模型/输出格式 | `--model "模型名"`、`--output-format text/json/stream-json` |
| 恢复历史会话      | `agent resume` 或 `agent --resume=id` |
| 交给云端继续跑    | 在消息前加 `&` |

安装好 Cursor CLI 后，在项目目录下直接运行 `agent` 即可开始使用。

---

<div style="display: flex; justify-content: space-between; align-items: center; margin: 40px 0; padding: 20px; background: #f5f5f5; border-radius: 8px; flex-wrap: wrap;">
  <div style="flex: 1; min-width: 150px;">
    <p style="margin: 0; color: #666; font-size: 14px;">上一篇</p>
    <p style="margin: 5px 0 0 0;">
      <a href="quick-reference.md" style="color: #0366d6; text-decoration: none; font-weight: 500;">← Cursor 快速参考手册</a>
    </p>
  </div>
  <div style="flex: 1; text-align: center; min-width: 150px;">
    <p style="margin: 0;">
      <a href="../README.md" style="color: #0366d6; text-decoration: none; font-weight: 500;">🏠 返回教程索引</a>
    </p>
  </div>
  <div style="flex: 1; text-align: right; min-width: 150px;">
    <p style="margin: 0; color: #666; font-size: 14px;">下一篇</p>
    <p style="margin: 5px 0 0 0;">
      <a href="advanced-features.md" style="color: #0366d6; text-decoration: none; font-weight: 500;">Cursor 高级功能指南 →</a>
    </p>
  </div>
</div>
