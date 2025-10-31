@echo off
title Firepit Manager
cd /d "%USERPROFILE%\FirepitManager"
echo.
echo ========================================
echo    ?? FIREPIT MANAGER LAUNCHER
echo ========================================
echo.
echo Starting application...
python src\main.py
if errorlevel 1 (
    echo.
    echo ? Error launching application!
    pause
) else (
    echo.
    echo ? Application closed successfully
)
