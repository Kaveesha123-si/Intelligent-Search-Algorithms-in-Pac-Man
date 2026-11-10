# Q6 cornersHeuristic + Q7 foodHeuristic (goes into searchAgents.py)
# Excerpt of the final integrated code in Group_Project/search/. Not runnable on its own.
# Member 4: Wickramasinghe W.S.S.D (IT24400002) - Heuristic Design & Final Integration Lead

from typing import Any, Tuple

# Definition of search, pacman, and helper stubs for IDE linter / type-checking
# (Prevents red underline errors in VS Code when viewed standalone)
class search:
    pass

class pacman:
    pass

class CornersProblem:
    corners = ()
    walls = None

class FoodSearchProblem:
    heuristicInfo = {}
    startingGameState = None

def mazeDistance(point1, point2, gameState):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def cornersHeuristic(state: Any, problem: Any) -> int:
    """
    Q6: A heuristic for CornersProblem using problem relaxation (ignoring maze walls).
    Computes minimum Manhattan tour cost to visit all remaining corners.
    """
    corners = problem.corners  # Target corner coordinates
    position, visited = state
    "*** YOUR CODE HERE ***"
    # 1. Filter out already visited corners to obtain remaining target corners
    remaining = [c for c, v in zip(corners, visited) if not v]
    # 2. If all corners visited, heuristic estimate is 0
    if not remaining:
        return 0

    # Helper: Manhattan distance |x1 - x2| + |y1 - y2|
    def manhattan(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    # 3. Exhaustive search over remaining corner orders (at most 4! = 24 permutations)
    # Computes the exact optimal relaxed Traveling Salesperson tour
    def cheapestTour(current, todo):
        if not todo:
            return 0
        return min(manhattan(current, c) + cheapestTour(c, [r for r in todo if r != c])
                   for c in todo)

    return cheapestTour(position, remaining)


def foodHeuristic(state: Tuple[Tuple, Any], problem: Any) -> int:
    """
    Q7: Heuristic for FoodSearchProblem (Eating all food dots).
    Computes true maze distance to the farthest remaining food dot.
    """
    position, foodGrid = state
    "*** YOUR CODE HERE ***"
    # 1. Convert food boolean grid to list of remaining food coordinates
    food = foodGrid.asList()
    # 2. If no food left, heuristic estimate is 0
    if not food:
        return 0

    # 3. Memoization cache inside problem instance to avoid recomputing maze distances
    cache = problem.heuristicInfo.setdefault('distCache', {})

    def dist(a, b):
        key = (a, b)
        if key not in cache:
            # mazeDistance computes shortest BFS path respecting walls
            cache[key] = mazeDistance(a, b, problem.startingGameState)
        return cache[key]

    # 4. Admissible & Consistent: Cost to eat all dots >= distance to farthest dot
    return max(dist(position, f) for f in food)
