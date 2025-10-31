@echo off
title Git Pull - Firepit Manager
cd /d "%USERPROFILE%\FirepitManager"
echo.
echo ========================================
echo    ?? PULLING FROM GITHUB
echo ========================================
echo.

echo Fetching latest changes...
git fetch origin

echo.
echo Pulling changes...
git pull origin main

if errorlevel 1 (
    echo.
    echo ? Pull failed! Check for conflicts.
    pause
    exit /b 1
) else (
    echo.
    echo ? Successfully updated from GitHub!
    timeout /t 3
)
