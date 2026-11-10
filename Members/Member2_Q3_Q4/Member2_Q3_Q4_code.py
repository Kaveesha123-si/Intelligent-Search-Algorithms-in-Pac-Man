# Q3 UCS + Q4 A*  (goes into search.py)
# Member 2: Walimuniarachchi W.A.K.S (IT24103947) - Q3 Uniform Cost Search & Q4 A* Search
# Excerpt of the final integrated code in Group_Project/search/.

# Definition of util and SearchProblem for IDE linter / type-checking
# (Prevents red underline errors in VS Code when viewed standalone)
class util:
    class PriorityQueue:
        def push(self, item, priority): pass
        def pop(self): pass
        def isEmpty(self) -> bool: return False

class SearchProblem:
    def getStartState(self): pass
    def isGoalState(self, state) -> bool: pass
    def getSuccessors(self, state): pass

def nullHeuristic(state, problem=None):
    return 0


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
