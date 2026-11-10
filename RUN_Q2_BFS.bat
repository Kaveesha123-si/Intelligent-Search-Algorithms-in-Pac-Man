@echo off
title Q2: Breadth First Search (BFS) - Pac-Man
color 0B
cd /d "%~dp0Group_Project\search"
echo =====================================================================
echo   Running Q2: Breadth First Search (BFS) on mediumMaze
echo =====================================================================
echo.
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
echo.
echo Simulation complete.
pause
