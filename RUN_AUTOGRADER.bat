@echo off
title Autograder Verification - Group_AI_28
color 0E
cd /d "%~dp0Group_Project\search"
echo =====================================================================
echo           RUNNING PAC-MAN AUTOGRADER (SE3062 / IT3012)
echo                       GROUP: Group_AI_28
echo =====================================================================
echo.
python autograder.py
echo.
echo =====================================================================
echo Grading complete. Press any key to exit.
echo =====================================================================
pause > nul
