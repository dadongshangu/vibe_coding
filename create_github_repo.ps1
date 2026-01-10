# GitHub Repository Creation Script
# Usage: Run this script and follow the prompts

param(
    [string]$GitHubToken = "",
    [string]$RepoName = "vibe_coding",
    [string]$Username = "LingxunMeng"
)

# If no token provided, prompt user
if ([string]::IsNullOrEmpty($GitHubToken)) {
    Write-Host "Please provide your GitHub Personal Access Token" -ForegroundColor Yellow
    Write-Host "If you don't have one, visit: https://github.com/settings/tokens" -ForegroundColor Yellow
    $secureToken = Read-Host "Enter your GitHub Personal Access Token" -AsSecureString
    $BSTR = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($secureToken)
    $GitHubToken = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($BSTR)
}

# API request to create repository
$headers = @{
    "Authorization" = "token $GitHubToken"
    "Accept" = "application/vnd.github.v3+json"
}

$body = @{
    name = $RepoName
    description = "Tutorials for learning Vibe Coding, Cursor and other tools"
    private = $true
} | ConvertTo-Json

try {
    Write-Host "Creating GitHub repository..." -ForegroundColor Green
    $response = Invoke-RestMethod -Uri "https://api.github.com/user/repos" -Method Post -Headers $headers -Body $body -ContentType "application/json"
    
    Write-Host "Repository created successfully!" -ForegroundColor Green
    Write-Host "Repository URL: $($response.html_url)" -ForegroundColor Cyan
    
    # Add remote repository
    Write-Host "Adding remote repository..." -ForegroundColor Green
    git remote add origin $response.clone_url
    
    # Push code
    Write-Host "Pushing code..." -ForegroundColor Green
    git push -u origin master
    
    Write-Host "Done!" -ForegroundColor Green
} catch {
    Write-Host "Error: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "Please check if your token has permission to create repositories" -ForegroundColor Yellow
    if ($_.Exception.Response) {
        $reader = New-Object System.IO.StreamReader($_.Exception.Response.GetResponseStream())
        $responseBody = $reader.ReadToEnd()
        Write-Host "Response: $responseBody" -ForegroundColor Red
    }
}
