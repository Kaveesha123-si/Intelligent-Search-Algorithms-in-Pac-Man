@echo off
title Run All Pac-Man Windows Simultaneously - Group_AI_28
color 0E
cd /d "%~dp0Group_Project\search"

echo =====================================================================
echo       LAUNCHING ALL PAC-MAN SIMULATIONS SIMULTANEOUSLY (AT ONCE)
echo                   GROUP: Group_AI_28
echo =====================================================================
echo.
echo Launching 6 Pac-Man windows at the exact same time...

start "Q1: DFS (mediumMaze)" python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs
start "Q2: BFS (mediumMaze)" python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
start "Q3: UCS (mediumMaze)" python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
start "Q4: A* Search (bigMaze)" python pacman.py -l bigMaze -z 0.5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
start "Q5 and Q6: Corners Problem" python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
start "Q7: Food Search" python pacman.py -l trickySearch -p AStarFoodSearchAgent

echo.
echo All 6 Pac-Man game windows have been launched simultaneously!
echo You can arrange or compare them on your screen.
echo =====================================================================
