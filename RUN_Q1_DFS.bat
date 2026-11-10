@echo off
title Q1: Depth First Search (DFS) - Pac-Man
color 0A
cd /d "%~dp0Group_Project\search"
echo =====================================================================
echo   Running Q1: Depth First Search (DFS) on mediumMaze
echo =====================================================================
echo.
python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs
echo.
echo Simulation complete.
pause
