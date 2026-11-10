@echo off
title Q3: Uniform Cost Search (UCS) - Pac-Man
color 0C
cd /d "%~dp0Group_Project\search"
echo =====================================================================
echo   Running Q3: Uniform Cost Search (UCS) on mediumMaze
echo =====================================================================
echo.
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
echo.
echo Simulation complete.
pause
