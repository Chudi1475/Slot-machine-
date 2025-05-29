while ($true) {
    $changed = git status --porcelain
    if ($changed) {
        git add .
        git commit -m "Auto-commit: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
        git push
        Write-Host "Committed and pushed at $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
    } else {
        Write-Host "No changes detected at $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
    }
    Start-Sleep -Seconds 5
}
