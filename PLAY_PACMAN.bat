@echo off
title Pac-Man Search Algorithms - Group_AI_28
color 0A
cd /d "%~dp0Group_Project\search"

:MENU
cls
echo =====================================================================
echo           SE3062 / IT3012 - INTELLIGENT SYSTEMS (PAC-MAN)
echo                       GROUP: Group_AI_28
echo =====================================================================
echo.
echo   [1] Q1: Depth First Search (DFS) on mediumMaze
echo   [2] Q2: Breadth First Search (BFS) on mediumMaze
echo   [3] Q3: Uniform Cost Search (UCS) on mediumMaze
echo   [4] Q4: A* Search with Manhattan Heuristic on bigMaze
echo   [5] Q5: Corners Problem (BFS) on tinyCorners
echo   [6] Q6: Corners Heuristic (A* Search) on mediumCorners
echo   [7] Q7: Food Search with A* on trickySearch
echo   [8] Q8: Closest Dot Search on bigSearch
echo   -------------------------------------------------------------------
echo   [A] Run Full Autograder (Grading Check)
echo   [M] Play Pac-Man Manually (Arrow Keys)
echo   [S] Run All Simulations SIMULTANEOUSLY (At the same time)
echo   [0] Exit
echo.
echo =====================================================================
choice /C 12345678AMS0 /N /M "Press a key [1-8, A, M, S, or 0]: "

if errorlevel 12 exit
if errorlevel 11 goto RUN_SIMULTANEOUS
if errorlevel 10 goto PLAY_MANUAL
if errorlevel 9 goto RUN_AUTO
if errorlevel 8 goto RUN_Q8
if errorlevel 7 goto RUN_Q7
if errorlevel 6 goto RUN_Q6
if errorlevel 5 goto RUN_Q5
if errorlevel 4 goto RUN_Q4
if errorlevel 3 goto RUN_Q3
if errorlevel 2 goto RUN_Q2
if errorlevel 1 goto RUN_Q1
goto MENU

:RUN_Q1
cls
echo =====================================================================
echo   Running Q1: Depth First Search (DFS) on mediumMaze...
echo =====================================================================
python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs
echo.
pause
goto MENU

:RUN_Q2
cls
echo =====================================================================
echo   Running Q2: Breadth First Search (BFS) on mediumMaze...
echo =====================================================================
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
echo.
pause
goto MENU

:RUN_Q3
cls
echo =====================================================================
echo   Running Q3: Uniform Cost Search (UCS) on mediumMaze...
echo =====================================================================
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
echo.
pause
goto MENU

:RUN_Q4
cls
echo =====================================================================
echo   Running Q4: A* Search on bigMaze...
echo =====================================================================
python pacman.py -l bigMaze -z 0.5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
echo.
pause
goto MENU

:RUN_Q5
cls
echo =====================================================================
echo   Running Q5: Corners Problem (BFS) on tinyCorners...
echo =====================================================================
python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
echo.
pause
goto MENU

:RUN_Q6
cls
echo =====================================================================
echo   Running Q6: Corners Heuristic (A* Search) on mediumCorners...
echo =====================================================================
python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
echo.
pause
goto MENU

:RUN_Q7
cls
echo =====================================================================
echo   Running Q7: Food Search with A* on trickySearch
echo =====================================================================
echo.
echo [*] Calculating optimal path across 4,137 search nodes with A*...
echo [*] Please wait 4-6 seconds -- Pac-Man is computing in memory
echo     and the graphical window will start moving right after!
echo.
python pacman.py -l trickySearch -p AStarFoodSearchAgent
echo.
pause
goto MENU

:RUN_Q8
cls
echo =====================================================================
echo   Running Q8: Closest Dot Search on bigSearch...
echo =====================================================================
python pacman.py -l bigSearch -p ClosestDotSearchAgent -z 0.5
echo.
pause
goto MENU

:PLAY_MANUAL
cls
echo =====================================================================
echo   Starting Manual Pac-Man (Use Arrow Keys to move)...
echo =====================================================================
python pacman.py
echo.
pause
goto MENU

:RUN_AUTO
cls
echo =====================================================================
echo   Running Autograder...
echo =====================================================================
python autograder.py
echo.
pause
goto MENU

:RUN_SIMULTANEOUS
cls
call "%~dp0RUN_ALL_SIMULTANEOUS.bat"
goto MENU
