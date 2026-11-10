@echo off
title Q8: Closest Dot Search - Pac-Man
color 0B
cd /d "%~dp0Group_Project\search"
echo =====================================================================
echo   Running Q8: Closest Dot Search on bigSearch
echo =====================================================================
echo.
python pacman.py -l bigSearch -p ClosestDotSearchAgent -z 0.5
echo.
echo Simulation complete.
pause
