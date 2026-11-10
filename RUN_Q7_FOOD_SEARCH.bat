@echo off
title Q7: Food Search - Pac-Man
color 0F
cd /d "%~dp0Group_Project\search"
echo =====================================================================
echo   Running Q7: Food Search with A* on trickySearch
echo =====================================================================
echo.
echo [*] Computing optimal path across 4,137 nodes using A* + foodHeuristic...
echo [*] Please wait 4-6 seconds for Pac-Man to begin moving in the window!
echo.
python pacman.py -l trickySearch -p AStarFoodSearchAgent
echo.
echo Simulation complete.
pause
