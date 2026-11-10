# SE3062 / IT3012: Intelligent Systems &ndash; Take-Home Assignment 04
## Search Algorithms in Pac-Man (UC Berkeley CS188 AI)

**Group ID:** `Group_AI_28`  
**Total Autograder Score:** `40 / 40 Marks (100%)`  
**Repository:** [https://github.com/IT24100131/SE3062-Intelligent-Systems](https://github.com/IT24100131/SE3062-Intelligent-Systems)

---

## 👥 Group Members & Task Allocation

| Member | Student ID | Assigned Questions | Feature Branch | Core Files Modified |
| :--- | :--- | :--- | :--- | :--- |
| **Basnayake K.S** | `IT24100131` | **Q1: DFS & Q2: BFS** (Uninformed Search, Stack & Queue) | `feature/dfs-bfs` | `search.py` |
| **Walimuniarachchi W.A.K.S** | `IT24103947` | **Q3: UCS & Q4: A\*** (Cost-sensitive, PriorityQueue, $f=g+h$) | `feature/ucs-astar` | `search.py` |
| **Gajanayake H.K.D.W.R** | `IT24510235` | **Q5: CornersProblem** (Compact & hashable state space representation) | `feature/corners` | `searchAgents.py` |
| **Wickramasinghe W.S.S.D** | `IT24400002` | **Q6: Corners Heuristic & Q7: Food Heuristic** (+ Git Lead & Packaging) | `feature/heuristics` | `searchAgents.py` |

---

## 📊 Autograder Score Summary

| Question | Algorithm / Problem | Target Layout | Max Threshold | Expanded Nodes / Score | Marks | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Q1** | Depth First Search (DFS) | `mediumMaze` | Graph Search | 146 nodes (Length: 130) | **4 / 4** | ✅ PASS |
| **Q2** | Breadth First Search (BFS) | `mediumMaze` | Optimal | 269 nodes (Length: 68) | **4 / 4** | ✅ PASS |
| **Q3** | Uniform Cost Search (UCS) | Varying Costs | Optimal | Optimal path across all costs | **4 / 4** | ✅ PASS |
| **Q4** | A* Search | `bigMaze` | $f(n)=g(n)+h(n)$ | 221 nodes (Optimal Cost: 210) | **4 / 4** | ✅ PASS |
| **Q5** | Corners Problem Representation | `tinyCorner` | Representation | Solution length: 28 | **8 / 8** | ✅ PASS |
| **Q6** | Corners Heuristic | `mediumCorners` | $\le 1200$ nodes | **741 nodes** (Optimal: 106) | **8 / 8** | ✅ PASS |
| **Q7** | Food Search Heuristic | `trickySearch` | $\le 9000$ nodes | **4137 nodes** (Optimal: 60) | **8 / 8** | ✅ PASS |
| **Total** | **Full Autograder Score** | | | | **40 / 40** | **100%** |

---

## 📂 Repository Structure

```text
├── Group_Project/
│   ├── README.md                  # Project execution guide
│   ├── autograder_logs/           # Full autograder terminal logs
│   └── search/                    # Berkeley Pac-Man core framework
│       ├── search.py              # Q1–Q4 implementations (DFS, BFS, UCS, A*)
│       ├── searchAgents.py        # Q5–Q7 implementations (CornersProblem, heuristics)
│       ├── pacman.py              # Game engine
│       ├── util.py                # Data structures (Stack, Queue, PriorityQueue)
│       └── autograder.py          # Berkeley autograder
│
├── Members/                       # Individual member packages & viva prep
│   ├── Member1_Q1_Q2/             # Member 1 code extract & README guide
│   ├── Member2_Q3_Q4/             # Member 2 code extract & README guide
│   ├── Member3_Q5/                # Member 3 code extract & README guide
│   └── Member4_Q6_Q7/             # Member 4 code extract & README guide
│
├── Report/                        # Report generation source, HTML, PDF & figures
│   ├── Group_AI_28_Report.html    # Standalone HTML report
│   ├── Group_AI_28_Report.pdf     # High-res compiled PDF report
│   └── images/                    # Verified autograder & Git execution screenshots
│
└── Submission/                    # Final submission files according to assignment rubric
    ├── Group_AI_28_Code.zip       # Zip archive with ONLY search.py and searchAgents.py
    └── Group_AI_28_Report.pdf     # Standalone PDF report for CourseWeb submission
```

---

## 🚀 Quick Start & Verification

### 1. Run Complete Autograder Suite
```bash
cd Group_Project/search
python autograder.py --no-graphics
```

### 2. Run Individual Questions
```bash
python autograder.py -q q1    # Q1: DFS
python autograder.py -q q2    # Q2: BFS
python autograder.py -q q3    # Q3: UCS
python autograder.py -q q4    # Q4: A*
python autograder.py -q q5    # Q5: CornersProblem
python autograder.py -q q6    # Q6: cornersHeuristic
python autograder.py -q q7    # Q7: foodHeuristic
```

### 3. Visual Pac-Man Simulation
```bash
# Q6: Corners Problem with A*
python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5

# Q7: Food Search with A*
python pacman.py -l trickySearch -p AStarFoodSearchAgent
```

---

## 🎓 Academic Integrity & Declaration
All solutions and heuristic mathematical formulations were engineered and implemented in accordance with SLIIT academic integrity standards. External AI aids utilized during preliminary analysis have been declared within the final report.
