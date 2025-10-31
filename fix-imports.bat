@echo off
title Fix FirepitManager Imports
cd /d "%USERPROFILE%\FirepitManager"

echo.
echo ========================================
echo    FIXING IMPORT ERRORS
echo ========================================
echo.

echo Fixing component_manager.py...
powershell -Command "(Get-Content 'src\gui\components\component_manager.py') -replace 'from \.\.database\.models import Component', 'from database.models import Component' | Set-Content 'src\gui\components\component_manager.py'"

echo.
echo ? Import fixed!
echo.
echo Now testing the app...
echo.
python src\main.py

if errorlevel 1 (
    echo.
    echo ? Still have errors - check the output above
    pause
) else (
    echo.
    echo ? App launched successfully!
)
