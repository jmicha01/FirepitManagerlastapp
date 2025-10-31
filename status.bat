@echo off
title Git Status - Firepit Manager
cd /d "%USERPROFILE%\FirepitManager"
echo.
echo ========================================
echo    ?? GIT STATUS
echo ========================================
echo.

echo Current Branch:
git branch --show-current

echo.
echo Recent Commits:
git log --oneline -5

echo.
echo ========================================
echo Changed Files:
echo ========================================
git status

echo.
echo ========================================
echo Remote Repository:
echo ========================================
git remote -v

echo.
pause
