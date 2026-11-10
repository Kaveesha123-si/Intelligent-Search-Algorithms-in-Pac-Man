@echo off
title Run All Pac-Man Visual Demonstrations - Group_AI_28
color 0B
cd /d "%~dp0Group_Project\search"

echo =====================================================================
echo       RUNNING ALL PAC-MAN VISUAL DEMONSTRATIONS (Q1 - Q7)
echo                   GROUP: Group_AI_28
echo =====================================================================
echo.
echo [1/6] Running Q1: Depth First Search (DFS) on mediumMaze...
python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs
timeout /t 2 >nul

echo.
echo [2/6] Running Q2: Breadth First Search (BFS) on mediumMaze...
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
timeout /t 2 >nul

echo.
echo [3/6] Running Q3: Uniform Cost Search (UCS) on mediumMaze...
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
timeout /t 2 >nul

echo.
echo [4/6] Running Q4: A* Search with Manhattan Heuristic on bigMaze...
python pacman.py -l bigMaze -z 0.5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
timeout /t 2 >nul

echo.
echo [5/6] Running Q5 and Q6: Corners Problem with A* on mediumCorners...
python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
timeout /t 2 >nul

echo.
echo [6/6] Running Q7: Food Search with A* on trickySearch...
python pacman.py -l trickySearch -p AStarFoodSearchAgent

echo.
echo =====================================================================
echo All visual demonstrations completed successfully!
echo =====================================================================
pause
