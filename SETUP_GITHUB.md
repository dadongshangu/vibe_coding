# GitHub 仓库设置说明

由于 GitHub CLI 未安装，有两种方式可以创建 GitHub 仓库并推送代码。

## 方式一：使用自动化脚本（推荐）

1. 获取 GitHub Personal Access Token：
   - 访问 https://github.com/settings/tokens
   - 点击 "Generate new token (classic)"
   - 选择 `repo` 权限
   - 生成并复制 token

2. 运行自动化脚本：
   ```powershell
   .\create_github_repo.ps1
   ```
   按照提示输入您的 token 和用户名即可。

## 方式二：手动创建（备选）

### 步骤 1: 在 GitHub 上创建仓库

1. 访问 [GitHub](https://github.com)
2. 点击右上角的 "+" 按钮，选择 "New repository"
3. 填写仓库信息：
   - **Repository name**: `vibe_coding`
   - **Description**: 学习 Vibe Coding、Cursor 等功能的教程
   - **Visibility**: 选择 **Private**（私有）
   - **不要**勾选 "Initialize this repository with a README"（因为本地已有）
4. 点击 "Create repository"

### 步骤 2: 添加远程仓库并推送

创建仓库后，GitHub 会显示仓库 URL。请执行以下命令（将 `YOUR_USERNAME` 替换为您的 GitHub 用户名）：

```bash
# 添加远程仓库
git remote add origin https://github.com/YOUR_USERNAME/vibe_coding.git

# 推送代码到远程仓库
git push -u origin master
```

如果您的 GitHub 账户启用了双因素认证，可能需要使用 Personal Access Token 代替密码。

### 步骤 3: 验证

推送成功后，访问 `https://github.com/YOUR_USERNAME/vibe_coding` 查看您的仓库。
