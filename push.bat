@echo off
title Git Push - Firepit Manager
cd /d "%USERPROFILE%\FirepitManager"
echo.
echo ========================================
echo    ?? PUSHING TO GITHUB
echo ========================================
echo.

REM Check for changes
git status --short
if errorlevel 1 (
    echo ? Git error detected!
    pause
    exit /b 1
)

echo.
set /p message="Enter commit message (or press Enter for default): "
if "%message%"=="" set message=Update: Code changes

echo.
echo Adding all changes...
git add .

echo Committing with message: %message%
git commit -m "%message%"

echo Pushing to GitHub...
git push origin main

if errorlevel 1 (
    echo.
    echo ? Push failed! Check your connection or credentials.
    pause
    exit /b 1
) else (
    echo.
    echo ? Successfully pushed to GitHub!
    timeout /t 3
)
