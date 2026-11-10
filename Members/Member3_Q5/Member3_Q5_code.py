# Q5 CornersProblem (goes into searchAgents.py)
# Excerpt of the final integrated code in Group_Project/search/. Not runnable on its own.
# Member 3: Gajanayake H.K.D.W.R (IT24510235) - Q5 Finding All the Corners (Problem Representation)

from typing import Any

# Definition of search, pacman, Directions, and Actions for IDE linter / type-checking
# (Prevents red underline errors in VS Code when viewed standalone)
class search:
    class SearchProblem:
        pass

class pacman:
    class GameState:
        def getWalls(self): pass
        def getPacmanPosition(self): pass
        def hasFood(self, x, y): pass

class Directions:
    NORTH = 'North'
    SOUTH = 'South'
    EAST = 'East'
    WEST = 'West'

class Actions:
    @staticmethod
    def directionToVector(action): return (0, 0)


class CornersProblem(search.SearchProblem):
    """
    This search problem finds paths through all four corners of a layout.

    You must select a suitable state space and successor function.
    """

    def __init__(self, startingGameState: pacman.GameState):
        """
        Stores the walls, pacman's starting position and corners.
        """
        self.walls = startingGameState.getWalls()
        self.startingPosition = startingGameState.getPacmanPosition()
        top, right = self.walls.height - 2, self.walls.width - 2
        self.corners = ((1, 1), (1, top), (right, 1), (right, top))
        for corner in self.corners:
            if not startingGameState.hasFood(*corner):
                print('Warning: no food in corner ' + str(corner))
        self._expanded = 0 # DO NOT CHANGE; Number of search nodes expanded

    def getStartState(self):
        """
        Returns the start state (in your state space, not the full Pacman state space)
        """
        "*** YOUR CODE HERE ***"
        # State representation: (currentPosition, visitedCornersTuple)
        # Check if the starting position is already on any corner
        visited = tuple(self.startingPosition == c for c in self.corners)
        return (self.startingPosition, visited)

    def isGoalState(self, state: Any):
        """
        Returns whether this search state is a goal state of the problem.
        The goal is reached when all four corners have been visited.
        """
        "*** YOUR CODE HERE ***"
        # Goal test: True if all 4 corners in tuple are True (visited)
        return all(state[1])

    def getSuccessors(self, state: Any):
        """
        Returns successor states, the actions they require, and a cost of 1.
        """
        successors = []
        # 1. Try moving in all 4 cardinal directions
        for action in [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]:
            (x, y), visited = state
            dx, dy = Actions.directionToVector(action)
            nextx, nexty = int(x + dx), int(y + dy)

            # 2. Check if the next position is free (not a wall)
            if not self.walls[nextx][nexty]:
                nextPos = (nextx, nexty)
                # 3. Update visited corners: True if already visited or newly reached
                newVisited = tuple(v or nextPos == c for v, c in zip(visited, self.corners))
                # 4. Successor triple: (new_state, action, stepCost=1)
                successors.append(((nextPos, newVisited), action, 1))

        self._expanded += 1  # Track search node expansions
        return successors

    def getCostOfActions(self, actions):
        """
        Returns the cost of a particular sequence of actions.  If those actions
        include an illegal move, return 999999.  This is implemented for you.
        """
        if actions == None: return 999999
        x, y = self.startingPosition
        for action in actions:
            dx, dy = Actions.directionToVector(action)
            x, y = int(x + dx), int(y + dy)
            if self.walls[x][y]: return 999999
        return len(actions)
