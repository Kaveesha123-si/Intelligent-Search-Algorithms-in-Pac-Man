# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # 1. Initialize LIFO Stack for DFS (deepest nodes explored first)
    fringe = util.Stack()
    # 2. Push start state and empty action path: (state, [actions])
    fringe.push((problem.getStartState(), []))
    # 3. Track visited states to prevent cycles/infinite loops (Graph Search)
    expanded = set()

    # 4. Explore until stack is empty
    while not fringe.isEmpty():
        # Pop the latest inserted node (LIFO order)
        state, path = fringe.pop()

        # Goal test: return action path if goal reached
        if problem.isGoalState(state):
            return path

        # Expand unvisited state to find valid neighbors
        if state not in expanded:
            expanded.add(state)  # Mark current state as visited
            for successor, action, _ in problem.getSuccessors(state):
                if successor not in expanded:
                    # Push next state with updated path onto stack
                    fringe.push((successor, path + [action]))

    return []  # Return empty list if no path found

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # 1. Initialize FIFO Queue for BFS (shallowest nodes explored first)
    fringe = util.Queue()
    # 2. Push start state and empty action path: (state, [actions])
    fringe.push((problem.getStartState(), []))
    # 3. Track visited states to prevent revisiting nodes (Graph Search)
    expanded = set()

    # 4. Explore level-by-level until queue is empty
    while not fringe.isEmpty():
        # Pop the earliest inserted node (FIFO order)
        state, path = fringe.pop()

        # Goal test: return optimal path if goal reached
        if problem.isGoalState(state):
            return path

        # Expand unvisited state to find valid neighbors
        if state not in expanded:
            expanded.add(state)  # Mark current state as visited
            for successor, action, _ in problem.getSuccessors(state):
                if successor not in expanded:
                    # Push next state with updated path into queue
                    fringe.push((successor, path + [action]))

    return []  # Return empty list if no path found

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # 1. Initialize PriorityQueue ordered by cumulative path cost g(n)
    fringe = util.PriorityQueue()
    # 2. Push start state: item = (state, [actions], cumulativeCost), priority = cost 0
    fringe.push((problem.getStartState(), [], 0), 0)
    # 3. Track visited states to prevent redundant expansions
    expanded = set()

    # 4. Pop node with least accumulated cost first
    while not fringe.isEmpty():
        state, path, cost = fringe.pop()

        # Goal test: return optimal path once popped from fringe
        if problem.isGoalState(state):
            return path

        # Expand unvisited state to explore successors
        if state not in expanded:
            expanded.add(state)  # Mark current state as visited
            for successor, action, stepCost in problem.getSuccessors(state):
                if successor not in expanded:
                    newCost = cost + stepCost  # Accumulate step cost g(n)
                    # Push successor with priority equal to total path cost
                    fringe.push((successor, path + [action], newCost), newCost)

    return []  # Return empty list if no path found

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()
    # 1. Initialize PriorityQueue ordered by combined cost f(n) = g(n) + h(n)
    fringe = util.PriorityQueue()
    # 2. Push start state with initial priority f(start) = 0 + h(start)
    fringe.push((start, [], 0), heuristic(start, problem))
    # 3. Track visited states to guarantee optimality
    expanded = set()

    # 4. Pop node with lowest f(n) first
    while not fringe.isEmpty():
        state, path, cost = fringe.pop()

        # Goal test: return optimal path once popped from fringe
        if problem.isGoalState(state):
            return path

        # Expand unvisited state to explore successors
        if state not in expanded:
            expanded.add(state)  # Mark current state as visited
            for successor, action, stepCost in problem.getSuccessors(state):
                if successor not in expanded:
                    newCost = cost + stepCost  # Actual path cost g(n)
                    # Priority = g(n) + h(n) (accumulated cost + heuristic estimate)
                    priority = newCost + heuristic(successor, problem)
                    fringe.push((successor, path + [action], newCost), priority)

    return []  # Return empty list if no path found


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
