param (
    [string]$filePath
)

if (-Not (Test-Path -Path $filePath)) {
    Write-Host "File does not exist: $filePath"
    exit 1
}

icacls.exe $filePath /reset
icacls.exe $filePath /grant:r "$($env:username):(r)"
icacls.exe $filePath /inheritance:r

Write-Host "Permissions updated for file: $filePath"
