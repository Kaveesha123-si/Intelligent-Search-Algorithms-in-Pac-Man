# Member 3 - Q5 CornersProblem (Problem Representation)

**Name:** Gajanayake H.K.D.W.R  |  **Student ID:** IT24510235  |  **Group:** Group_AI_28

---

## 1. Responsibilities & Assigned Task
Responsible for **Q5: Finding All the Corners (Problem Representation)** in `searchAgents.py`.
The objective is to formulate a search problem whose goal is to find the shortest path that touches all four corners of the maze.

---

## 2. Files and Methods Edited
- **Target File:** `searchAgents.py`
- **Class:** `CornersProblem(search.SearchProblem)`
- **Methods Implemented:**
  1. `getStartState(self)`: Initializes the search state from Pac-Man's starting coordinates.
  2. `isGoalState(self, state)`: Evaluates if all 4 corners have been visited.
  3. `getSuccessors(self, state)`: Generates valid legal next states and updates corner visitation status.
- **Standalone Code Extract:** `Member3_Q5_code.py`

---

## 3. Technical Implementation & Design Decisions

### State Space Representation
- **State Definition:** `((x, y), (c1_visited, c2_visited, c3_visited, c4_visited))`
  - `(x, y)`: Pac-Man's current grid coordinates (integer pair).
  - `visitedCorners`: An immutable 4-tuple of booleans indicating whether each of the 4 corners has been reached.
- **Why this design?**
  1. **Compact & Hashable:** Python `tuple` of booleans is hashable, enabling O(1) membership testing in the `expanded` set of graph search algorithms.
  2. **No Redundant State Data:** It strictly excludes walls and full GameState objects, avoiding massive memory bloat.
  3. **State Space Bounded Size:** Total state space is bounded by $|V| \times 2^4 = 16 \times |V|$ states (where $|V|$ is the number of reachable maze tiles), making graph search extremely fast and computationally tractable.

### Successor Bookkeeping
- For each legal cardinal direction (`North`, `South`, `East`, `West`), if the next cell is not a wall (`not self.walls[nextx][nexty]`):
  - The next position `nextPos = (nextx, nexty)` is computed.
  - The corner visitation tuple is updated: `newVisited = tuple(v or nextPos == c for v, c in zip(visited, self.corners))`.
  - The successor tuple `((nextPos, newVisited), action, 1)` is returned with unit step cost 1.

### Goal Test
- `all(state[1])`: Returns `True` if and only if all four boolean flags in the visitation tuple are `True`.

---

## 4. Verification & Autograder Results
- **Autograder Score:** `8/8` marks (Autograder command: `python autograder.py -q q5`).
- **Test Results:**
  - `test_cases/q5/corner_tiny_corner.test`: PASS (Solution length: 28, full marks awarded).

---

## 5. How to Run & Verify Locally
Run the following commands inside `Group_Project/search/`:
```bash
# Run autograder for Q5
python autograder.py -q q5

# Run visual Pac-Man game with BFS on tinyCorner
python pacman.py -l tinyCorner -p SearchAgent -a fn=bfs,prob=CornersProblem

# Run visual Pac-Man game with BFS on mediumCorners
python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
```

---

## 6. Viva Cheat-Sheet (Rapid-Fire Defense Questions)

1. **Why can't we store the entire `GameState` or maze walls in the state?**
   - *Answer:* The walls never change during search, so storing them is redundant and consumes unnecessary memory. Storing `GameState` would make the state unhashable or very expensive to copy/compare, destroying search efficiency.

2. **How large is the state space of `CornersProblem`?**
   - *Answer:* If the maze has $W \times H$ positions and Pacman can occupy around $|V|$ non-wall spaces, each position can be paired with any of $2^4 = 16$ corner visitation subsets. The total state space is exactly $16 \times |V|$ states.

3. **Why use an immutable `tuple` rather than a `list` or `set` for visited corners?**
   - *Answer:* Graph search algorithms (DFS, BFS, UCS, A*) maintain an `expanded` set. In Python, sets require keys to be hashable (`__hash__`). Lists and sets are mutable and unhashable, whereas tuples are immutable and hashable.

4. **What happens if Pac-Man starts directly on top of a corner?**
   - *Answer:* `getStartState()` explicitly initializes the visited tuple by checking `self.startingPosition == c for c in self.corners`. Thus, if Pac-Man starts on a corner, that corner is immediately flagged as `True`.

---

## 7. Team Workflow & Collaboration
- **Git Feature Branch:** `feature/corners`
- **Peer Review Responsibility:** Review pull request and test cases of **Member 4 (Q6 & Q7 Heuristics)**.
- **Viva Preparation:** Thoroughly understand Q1-Q7 algorithms to support any team question during the oral evaluation.

---

## 8. Individual Git Commit History (Recommended Commits)
- `commit 1`: "Q5: Design hashable (pos, visitedCorners) state representation for CornersProblem"
- `commit 2`: "Q5: Implement getStartState and isGoalState checking all visited flags"
- `commit 3`: "Q5: Implement getSuccessors with legal wall checks and corner tracking"
- `commit 4`: "Q5: Validate test_cases/q5/corner_tiny_corner.test (8/8 marks)"

---

## 9. AI Usage Declaration
- **Tools Used:** Anthropic Claude & Google Gemini.
- **Scope:** Used for reviewing the tuple state representation formulation and checking edge cases for starting states on corner positions. Code was manually tested and debugged locally.
