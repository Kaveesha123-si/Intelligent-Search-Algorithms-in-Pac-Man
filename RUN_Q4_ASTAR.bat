@echo off
title Q4: A* Search - Pac-Man
color 0D
cd /d "%~dp0Group_Project\search"
echo =====================================================================
echo   Running Q4: A* Search on bigMaze
echo =====================================================================
echo.
python pacman.py -l bigMaze -z 0.5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
echo.
echo Simulation complete.
pause
