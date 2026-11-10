@echo off
title Q5: Corners Problem (BFS) - Pac-Man
color 0E
cd /d "%~dp0Group_Project\search"
echo =====================================================================
echo   Running Q5: Corners Problem (BFS) on tinyCorners
echo =====================================================================
echo.
python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
echo.
echo Simulation complete.
pause
