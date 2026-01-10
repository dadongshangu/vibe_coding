# GitHub 仓库创建脚本
# 使用方法：在 PowerShell 中运行此脚本，并按照提示输入您的 GitHub Personal Access Token

param(
    [string]$GitHubToken = "",
    [string]$RepoName = "vibe_coding",
    [string]$Username = ""
)

# 如果没有提供 token，提示用户输入
if ([string]::IsNullOrEmpty($GitHubToken)) {
    Write-Host "请提供您的 GitHub Personal Access Token" -ForegroundColor Yellow
    Write-Host "如果没有 token，请访问: https://github.com/settings/tokens" -ForegroundColor Yellow
    $GitHubToken = Read-Host "请输入您的 GitHub Personal Access Token" -AsSecureString
    $GitHubToken = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($GitHubToken))
}

# 如果没有提供用户名，尝试从 git config 获取
if ([string]::IsNullOrEmpty($Username)) {
    $Username = git config user.name
    if ([string]::IsNullOrEmpty($Username)) {
        $Username = Read-Host "请输入您的 GitHub 用户名"
    }
}

# 创建仓库的 API 请求
$headers = @{
    "Authorization" = "token $GitHubToken"
    "Accept" = "application/vnd.github.v3+json"
}

$body = @{
    name = $RepoName
    description = "学习 Vibe Coding、Cursor 等功能的教程"
    private = $true
} | ConvertTo-Json

try {
    Write-Host "正在创建 GitHub 仓库..." -ForegroundColor Green
    $response = Invoke-RestMethod -Uri "https://api.github.com/user/repos" -Method Post -Headers $headers -Body $body -ContentType "application/json"
    
    Write-Host "仓库创建成功！" -ForegroundColor Green
    Write-Host "仓库 URL: $($response.html_url)" -ForegroundColor Cyan
    
    # 添加远程仓库
    Write-Host "正在添加远程仓库..." -ForegroundColor Green
    git remote add origin $response.clone_url
    
    # 推送代码
    Write-Host "正在推送代码..." -ForegroundColor Green
    git push -u origin master
    
    Write-Host "完成！" -ForegroundColor Green
} catch {
    Write-Host "错误: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "请检查您的 token 是否有创建仓库的权限" -ForegroundColor Yellow
}
