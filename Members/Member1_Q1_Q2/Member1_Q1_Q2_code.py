# =======================================================================
# Member 1 (IT24100131) - Q1 DFS & Q2 BFS Code
# Target file in project: Group_Project/search/search.py
# =======================================================================

# Definition of util and SearchProblem for IDE linter / type-checking
# (Prevents red underline errors in VS Code when viewed standalone)
class util:
    class Stack:
        def push(self, item): pass
        def pop(self): pass
        def isEmpty(self) -> bool: return False

    class Queue:
        def push(self, item): pass
        def pop(self): pass
        def isEmpty(self) -> bool: return False

class SearchProblem:
    def getStartState(self): pass
    def isGoalState(self, state) -> bool: pass
    def getSuccessors(self, state): pass


# -----------------------------------------------------------------------
# Q1: Depth First Search (DFS)
# -----------------------------------------------------------------------
def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.
    Graph-search DFS using util.Stack (LIFO).
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


# -----------------------------------------------------------------------
# Q2: Breadth First Search (BFS)
# -----------------------------------------------------------------------
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
