# Pac-Man Search (SE3062 / IT3012 Intelligent Systems Group Assignment)
**Group ID:** Group_AI_28  
**Total Autograder Score:** 40 / 40 Marks (100%)

---

## Team Division & Roles
| Member | Student ID | Responsibilities | Feature Branch | Target Files |
| :--- | :--- | :--- | :--- | :--- |
| **Member 1 (Basnayake K.S)** | IT24100131 | Q1 DFS & Q2 BFS (Graph Search with Stack & Queue) | `feature/dfs-bfs` | `search.py` |
| **Member 2 (Walimuniarachchi W.A.K.S)** | IT24103947 | Q3 UCS & Q4 A* (PriorityQueue with path costs & heuristics) | `feature/ucs-astar` | `search.py` |
| **Member 3 (Gajanayake H.K.D.W.R)** | IT24510235 | Q5 CornersProblem (State Space Representation & Successor Logic) | `feature/corners` | `searchAgents.py` |
| **Member 4 (Wickramasinghe W.S.S.D)** | IT24400002 | Q6 Corners Heuristic & Q7 Food Heuristic, Git Lead & Packaging | `feature/heuristics` | `searchAgents.py` |

---

## Quick Verification
Navigate to `Group_Project/search/` and execute:
```bash
# Run all questions Q1 through Q7 without graphics
python autograder.py --no-graphics

# Test specific questions
python autograder.py -q q1   # DFS (4/4)
python autograder.py -q q2   # BFS (4/4)
python autograder.py -q q3   # UCS (4/4)
python autograder.py -q q4   # A* (4/4)
python autograder.py -q q5   # CornersProblem (8/8)
python autograder.py -q q6   # cornersHeuristic (8/8)
python autograder.py -q q7   # foodHeuristic (8/8)
```

---

## Submission Artifacts
1. **Standalone PDF Report:** `Submission/Group_AI_28_Report.pdf` (meets all formatting, word count, screenshot, and declaration requirements).
2. **Code ZIP Archive:** `Submission/Group_AI_28_Code.zip` (contains ONLY `search.py` and `searchAgents.py`).
