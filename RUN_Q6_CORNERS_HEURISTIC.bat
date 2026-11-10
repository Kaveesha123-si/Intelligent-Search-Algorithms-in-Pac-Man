@echo off
title Q6: Corners Heuristic (A* Search) - Pac-Man
color 0E
cd /d "%~dp0Group_Project\search"
echo =====================================================================
echo   Running Q6: Corners Heuristic with A* on mediumCorners
echo =====================================================================
echo.
python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
echo.
echo Simulation complete.
pause
