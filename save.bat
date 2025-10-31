@echo off
title Quick Save - Firepit Manager
cd /d "%USERPROFILE%\FirepitManager"
color 0A
echo.
echo ========================================
echo    ?? QUICK SAVE TO GITHUB
echo ========================================
echo.

REM Show what will be saved
echo Files to be saved:
git status --short

echo.
set /p confirm="Save these changes? (Y/N): "
if /i not "%confirm%"=="Y" (
    echo Cancelled.
    timeout /t 2
    exit /b 0
)

echo.
set /p message="Commit message (Enter for timestamp): "
if "%message%"=="" (
    for /f "tokens=2-4 delims=/ " %%a in ('date /t') do (set mydate=%%c-%%a-%%b)
    for /f "tokens=1-2 delims=/:" %%a in ('time /t') do (set mytime=%%a%%b)
    set message=Save !mydate! !mytime!
)

echo.
echo Adding files...
git add .

echo Committing...
git commit -m "%message%"

echo Pushing...
git push origin main

if errorlevel 1 (
    echo.
    echo ? Quick save failed!
    pause
) else (
    echo.
    echo ? Quick save successful!
    timeout /t 2
)
