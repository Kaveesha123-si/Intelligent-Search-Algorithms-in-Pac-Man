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




import util

class SearchProblem:
   

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
       
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        
        util.raiseNotDefined()


def tinyMazeSearch(problem):
   
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
   
    
    # Q1 (Member 1 - IT24100131 Basnayake K.S): Graph-search DFS using util.Stack (LIFO).
    # Nodes are expanded deepest-first to find a path to the food goal.
    fringe = util.Stack() #create stack
    fringe.push((problem.getStartState(), []))  
    expanded = set() #Stores visited states
    while not fringe.isEmpty():
        state, path = fringe.pop() #Gets the last added state
        if problem.isGoalState(state): 
            return path #returns the path to the goal
        if state not in expanded:
            expanded.add(state) #marks state as visited
            for successor, action, _ in problem.getSuccessors(state): #Gets all the successors of the current state
                if successor not in expanded:
                    fringe.push((successor, path + [action]))
    return [] #Returns an empty path if the goal is not found

def breadthFirstSearch(problem: SearchProblem):
   
    # Q2 (Member 1 - IT24100131 Basnayake K.S): Graph-search BFS using util.Queue (FIFO).
    # Nodes are expanded level-by-level, guaranteeing optimal path for unit step costs.
    fringe = util.Queue()
    fringe.push((problem.getStartState(), []))
    expanded = set()#Stores visited states
    while not fringe.isEmpty():
        state, path = fringe.pop()#Gets the last added state
        if problem.isGoalState(state):
            return path
        if state not in expanded:
            expanded.add(state)#marks state as visited
            for successor, action, _ in problem.getSuccessors(state):#Gets all the successors of the current state
                if successor not in expanded:
                    fringe.push((successor, path + [action]))
    return []

def uniformCostSearch(problem: SearchProblem):
    
    # Q3 (Member 2 - IT24103947 Walimuniarachchi W.A.K.S): fringe is a PriorityQueue ordered by the accumulated path
    # cost g(n). A state is only finalised when it is popped (not when pushed),
    # which is what guarantees optimality with non-uniform step costs.
    fringe = util.PriorityQueue()
    fringe.push((problem.getStartState(), [], 0), 0) #Adds the start state with zero cost
    expanded = set() #Stores visited states
    while not fringe.isEmpty():
        state, path, cost = fringe.pop()
        if problem.isGoalState(state): 
            return path #Returns the path to the goal
        if state not in expanded:
            expanded.add(state)
            for successor, action, stepCost in problem.getSuccessors(state):#Gets all the successors of the current state
                if successor not in expanded:
                    newCost = cost + stepCost #Calculates the total cost
                    fringe.push((successor, path + [action], newCost), newCost)#Adds the successor to the fringe
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
   
    # Q4 (Member 2 - IT24103947 Walimuniarachchi W.A.K.S): same as UCS but the priority is f(n) = g(n) + h(n). With
    # nullHeuristic (h = 0) this degenerates to UCS; with an admissible and
    # consistent h it stays optimal while expanding fewer nodes.
    start = problem.getStartState()
    fringe = util.PriorityQueue()
    fringe.push((start, [], 0), heuristic(start, problem))#Adds the start state with heuristic priority
    expanded = set()#Stores visited states
    while not fringe.isEmpty():
        state, path, cost = fringe.pop()
        if problem.isGoalState(state):#Checks if the current state is the goal
            return path
        if state not in expanded:
            expanded.add(state)
            for successor, action, stepCost in problem.getSuccessors(state):#Gets all the successors of the current state
                if successor not in expanded:
                    newCost = cost + stepCost#Calculates the total cost
                    fringe.push((successor, path + [action], newCost),
                                newCost + heuristic(successor, problem))#Adds the successor to the fringe with the heuristic priority
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
