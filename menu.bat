@echo off
title Firepit Manager - Main Menu
color 0B
cd /d "%USERPROFILE%\FirepitManager"

:menu
cls
echo.
echo ========================================
echo     ?? FIREPIT MANAGER MENU
echo ========================================
echo.
echo  1. ?? Launch Application
echo  2. ?? Quick Save to GitHub
echo  3. ?? Check Git Status
echo  4. ?? Pull from GitHub
echo  5. ?? Push to GitHub (with message)
echo  6. ?? Open GitHub Repository
echo  7. ?? Open Project Folder
echo  8. ?? Reload PowerShell Profile
echo  9. ? Exit
echo.
echo ========================================
set /p choice="Select option (1-9): "

if "%choice%"=="1" goto launch
if "%choice%"=="2" goto save
if "%choice%"=="3" goto status
if "%choice%"=="4" goto pull
if "%choice%"=="5" goto push
if "%choice%"=="6" goto github
if "%choice%"=="7" goto folder
if "%choice%"=="8" goto reload
if "%choice%"=="9" goto exit
goto menu

:launch
cls
echo Launching Firepit Manager...
python src\main.py
pause
goto menu

:save
cls
call save.bat
pause
goto menu

:status
cls
call status.bat
goto menu

:pull
cls
call pull.bat
pause
goto menu

:push
cls
call push.bat
goto menu

:github
start https://github.com/jmicha01/FirepitManagerlastapp
goto menu

:folder
start .
goto menu

:reload
powershell -Command ". $PROFILE"
echo ? PowerShell profile reloaded
timeout /t 2
goto menu

:exit
exit
