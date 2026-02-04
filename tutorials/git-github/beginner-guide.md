# Git 与 GitHub 入门：Star、Clone、Fork 怎么选？

> 看到好项目该怎么“收着用”？一句话：**Star = 收藏，Clone = 下载到本地，Fork = 复制一份到你账号下再改。**

## 📋 目录

1. [一句话区别](#一句话区别)
2. [Star：收藏与发现](#star收藏与发现)
3. [Clone：把代码下载到本地](#clone把代码下载到本地)
4. [Fork：复制一份到你账号下](#fork复制一份到你账号下)
5. [“给自己用”该怎么选？](#给自己用该怎么选)
6. [常用 Git 命令速查](#常用-git-命令速查)
7. [小结](#小结)

---

## 一句话区别

| 操作 | 发生位置 | 你得到什么 | 典型用途 |
|------|----------|------------|----------|
| **Star** | 只在 GitHub 网页 | 项目出现在你的 “Starred” 列表里，方便以后找 | 收藏、支持作者、当书签 |
| **Clone** | 从 GitHub 到你的电脑 | 本地多了一个和仓库一样的文件夹 | 本地跑、看代码、自己改着玩（不打算推回原仓库） |
| **Fork** | 在 GitHub 上 | 你的账号下多了一个“复制出来的仓库” | 想自己改并保留在 GitHub、或给原项目提 PR |

- **Star** 不下载代码，只记一笔“我感兴趣”。
- **Clone** 下载代码到本机，原仓库和你本地没有持续关联（除非你自己加 remote）。
- **Fork** 在 GitHub 上复制一份到你账号，你可以在 Fork 里改、再 Clone 到本地，或向原项目提 Pull Request。

---

## Star：收藏与发现

**是什么**：在项目页点一下 “Star”，相当于“收藏”或“点赞”。代码不会下载，只是把这个项目记在你的 GitHub 个人页 “Starred repositories” 里。

**适合**：

- 觉得项目不错，以后想再找来看
- 支持作者（Star 数对开源项目很重要）
- 当“书签”，在 GitHub 里按主题浏览自己 Star 过的项目

**怎么用**：打开项目页面 → 右上角点 **Star**（再点一次可取消）。

**总结**：不涉及“用代码”，只涉及“在 GitHub 上留着入口”。

---

## Clone：把代码下载到本地

**是什么**：用 Git 把仓库**完整复制**到你当前电脑的某个文件夹里，得到一个和远程一致的本地仓库（含历史记录）。

**适合**：

- 只想在**本机**运行、阅读、学习
- 自己在本地改着玩，**不打算**把改动推回原作者的仓库
- 做一次性的“拖下来用”，不打算在 GitHub 上保留自己的一份

**怎么用**：

```bash
# 用 HTTPS（常见）
git clone https://github.com/用户名/仓库名.git

# 克隆到指定文件夹名
git clone https://github.com/用户名/仓库名.git 我的文件夹名
```

克隆后你会得到一个目录，里面就是完整项目。之后可以随意在本地改，但**默认没有写原仓库的权限**，你的改动只能留在本地，或推到你自己建的仓库（需自己加 `remote`）。

**总结**：把代码“下载到本地用”，不改变 GitHub 上任何仓库，也不自动在你账号下多一个仓库。

---

## Fork：复制一份到你账号下

**是什么**：在 **GitHub 网站上**点 “Fork”，会在**你的 GitHub 账号下**新建一个仓库，内容是当时原仓库的拷贝。之后这个 Fork 完全属于你，你可以再 Clone、改代码、推送，甚至给原项目提 PR。

**适合**：

- 想**在 GitHub 上保留自己的一份**，方便多设备同步、备份
- 打算**长期基于这个项目改**，并且可能给原项目提 Pull Request（PR）
- 想在自己的 Fork 里实验，不影响原仓库

**怎么用**：

1. 打开原项目页面 → 右上角点 **Fork** → 选择你的账号（若只有一个账号会直接创建）。
2. Fork 完成后，你会在 “Your repositories” 里看到这个新仓库，地址类似：`https://github.com/你的用户名/仓库名`。
3. 若要本地开发，再 **Clone 你自己的 Fork**：
   ```bash
   git clone https://github.com/你的用户名/仓库名.git
   ```
4. （可选）把原仓库加为 `upstream`，方便以后同步原项目的更新：
   ```bash
   cd 仓库名
   git remote add upstream https://github.com/原作者/仓库名.git
   # 之后拉取原仓库更新：git fetch upstream && git merge upstream/main
   ```

**总结**：Fork = 在 GitHub 上“复制一份到我名下”；要本地改就再 Clone 自己的 Fork；要给原作者贡献就提 PR。

---

## “给自己用”该怎么选？

可以按你的目标快速选：

| 你的目标 | 推荐做法 |
|----------|----------|
| 只是以后在 GitHub 上容易找到这个项目 | **Star** |
| 在本地跑一跑、看看代码、随便改改，不打算同步回网上 | **Clone** |
| 要在 GitHub 上有一份自己的拷贝，多设备同步或以后可能提 PR | **Fork**，再 **Clone 你的 Fork** |
| 想基于它做自己的项目，且不打算和原项目保持同步 | **Fork**（或 Fork 后删掉 upstream），然后当自己的仓库用 |

**简单决策**：

- 只收藏链接 → **Star**
- 只在本机用、不打算在 GitHub 上留一份 → **Clone**
- 要在 GitHub 上有一份、或可能给原项目做贡献 → **Fork**，再按需 Clone / 加 upstream

---

## 常用 Git 命令速查

克隆和日常“给自己用”时，下面这些就够用。

| 场景 | 命令 |
|------|------|
| 第一次把远程仓库拉到本地 | `git clone <仓库URL>` |
| 看当前状态（改了哪些文件） | `git status` |
| 把修改加入暂存区 | `git add 文件名` 或 `git add .` |
| 提交到本地 | `git commit -m "说明"` |
| 推送到远程（你已有推送权限的仓库） | `git push`（首次可 `git push -u origin main`） |
| 从远程拉取最新 | `git pull` |
| 看远程仓库地址 | `git remote -v` |
| 添加“原仓库”为 upstream（Fork 后同步用） | `git remote add upstream <原仓库URL>` |

**注意**：Clone 下来的仓库默认 `origin` 指向你克隆的那个地址；Fork 后 Clone 的是你 Fork 的地址，所以 `git push` 是推到你自己的 Fork，不会直接推到原仓库。要向原项目贡献，需要提 Pull Request（在 GitHub 网页上从你的 Fork 发起）。

---

## 小结

- **Star**：收藏项目，不下载代码，方便以后在 GitHub 上找。
- **Clone**：把代码下载到本机，本地用、本地改，不自动在 GitHub 上多一个仓库。
- **Fork**：在 GitHub 上复制一份到你账号下，可再 Clone、改、推送；要贡献就给原项目提 PR。

“给自己用”时：只收藏就 Star；只在本机用就 Clone；要在 GitHub 上有一份或可能参与贡献就 Fork，再 Clone 你的 Fork 即可。

---

<div style="display: flex; justify-content: space-between; align-items: center; margin: 40px 0; padding: 20px; background: #f5f5f5; border-radius: 8px; flex-wrap: wrap;">
  <div style="flex: 1; min-width: 150px;">
    <p style="margin: 0; color: #666; font-size: 14px;">上一篇</p>
    <p style="margin: 5px 0 0 0;">
      <a href="../cursor/advanced-features.md" style="color: #0366d6; text-decoration: none; font-weight: 500;">← Cursor 高级功能指南</a>
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
      <a href="../vibe-coding/beginner-guide.md" style="color: #0366d6; text-decoration: none; font-weight: 500;">Vibe Coding 初学者完全指南 →</a>
    </p>
  </div>
</div>
