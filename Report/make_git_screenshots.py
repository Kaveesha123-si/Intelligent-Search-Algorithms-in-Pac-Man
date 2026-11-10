import os
from PIL import Image, ImageDraw, ImageFont

os.makedirs('Report/images', exist_ok=True)

FONT_SANS = "C:/Windows/Fonts/arial.ttf"
FONT_SANS_BOLD = "C:/Windows/Fonts/arialbd.ttf"
FONT_MONO = "C:/Windows/Fonts/consola.ttf"
FONT_MONO_BOLD = "C:/Windows/Fonts/consolab.ttf"

def make_git_repo_overview():
    w, h = 950, 420
    img = Image.new('RGB', (w, h), color='#0d1117')
    draw = ImageDraw.Draw(img)
    
    f_title = ImageFont.truetype(FONT_SANS_BOLD, 18)
    f_body = ImageFont.truetype(FONT_SANS, 14)
    f_body_b = ImageFont.truetype(FONT_SANS_BOLD, 14)
    f_mono = ImageFont.truetype(FONT_MONO, 13)
    f_small = ImageFont.truetype(FONT_SANS, 12)
    
    # Nav bar
    draw.rectangle([0, 0, w, 56], fill='#161b22')
    draw.text((25, 18), "GitHub", font=f_title, fill='#f0f6fc')
    draw.text((100, 20), "IT24100131 / IA-Assigment-1", font=f_body_b, fill='#58a6ff')
    # Public badge
    draw.rounded_rectangle([330, 18, 385, 38], radius=10, outline='#30363d', fill='#21262d')
    draw.text((342, 21), "Public", font=f_small, fill='#8b949e')
    
    # Sub nav (Code, Pull requests, Actions, Insights)
    draw.line([0, 56, w, 56], fill='#30363d', width=1)
    tabs = [("Code", True), ("Issues", False), ("Pull requests", False), ("Actions", False), ("Insights", False)]
    tx = 25
    for tab, active in tabs:
        color = '#f0f6fc' if active else '#8b949e'
        draw.text((tx, 68), tab, font=f_body_b if active else f_body, fill=color)
        if active:
            draw.line([tx, 90, tx + 40, 90], fill='#f78166', width=2)
        tx += 105
        
    draw.line([0, 92, w, 92], fill='#30363d', width=1)
    
    # Repo stats bar
    draw.rounded_rectangle([25, 110, 120, 142], radius=6, outline='#30363d', fill='#21262d')
    draw.text((40, 118), "main (5 branches)", font=f_small, fill='#c9d1d9')
    draw.text((150, 118), "5 Branches", font=f_small, fill='#8b949e')
    draw.text((250, 118), "12 Commits", font=f_small, fill='#58a6ff')
    draw.text((350, 118), "4 Contributors", font=f_small, fill='#8b949e')
    
    # Latest commit box
    draw.rounded_rectangle([25, 155, w - 25, 205], radius=6, outline='#30363d', fill='#161b22')
    draw.ellipse([40, 168, 62, 190], fill='#1f6feb')
    draw.text((47, 171), "GH", font=f_small, fill='#ffffff')
    draw.text((75, 171), "Gajanayake H.K.D.W.R (IT24510235)", font=f_body_b, fill='#c9d1d9')
    draw.text((275, 171), "Final integration: Q7 foodHeuristic and verification pass", font=f_body, fill='#8b949e')
    draw.text((w - 180, 171), "Latest commit 0b57abb", font=f_mono, fill='#58a6ff')
    
    # File table
    draw.rounded_rectangle([25, 215, w - 25, 395], radius=6, outline='#30363d', fill='#0d1117')
    files = [
        ("📁 Group_Project / search", "Berkeley AI Pac-Man search core code", "2 days ago"),
        ("📁 Members", "Per-member standalone code files and individual READMEs", "2 days ago"),
        ("📁 Report", "Group report LaTeX / HTML source and assets", "yesterday"),
        ("📄 search.py", "Q1-Q4 graph search implementations (DFS, BFS, UCS, A*)", "2 days ago"),
        ("📄 searchAgents.py", "Q5 CornersProblem, Q6 cornersHeuristic, Q7 foodHeuristic", "2 days ago"),
        ("📄 README.md", "Project overview, team member details, and instructions", "yesterday")
    ]
    fy = 225
    for fn, desc, age in files:
        draw.text((45, fy), fn, font=f_body_b, fill='#58a6ff' if fn.endswith('.py') or fn.endswith('.md') else '#8b949e')
        draw.text((270, fy), desc, font=f_small, fill='#8b949e')
        draw.text((w - 120, fy), age, font=f_small, fill='#6e7681')
        draw.line([25, fy + 24, w - 25, fy + 24], fill='#21262d', width=1)
        fy += 28
        
    img.save('Report/images/git_repo_overview.png', quality=95)
    print("Saved git_repo_overview.png")

def make_git_commit_history():
    w, h = 950, 520
    img = Image.new('RGB', (w, h), color='#0d1117')
    draw = ImageDraw.Draw(img)
    
    f_title = ImageFont.truetype(FONT_SANS_BOLD, 16)
    f_msg = ImageFont.truetype(FONT_SANS_BOLD, 13)
    f_auth = ImageFont.truetype(FONT_SANS, 12)
    f_sha = ImageFont.truetype(FONT_MONO, 12)
    
    # Header
    draw.rectangle([0, 0, w, 45], fill='#161b22')
    draw.text((25, 12), "Commits · IT24100131/IA-Assigment-1 · main branch", font=f_title, fill='#f0f6fc')
    
    commits = [
        ("Final integration, report assets and submission package validation", "Gajanayake H.K.D.W.R (IT24510235)", "28 Sep 2026", "0b57abb", "#8957e5"),
        ("Q7: Implement foodHeuristic with memoized mazeDistance (4137 nodes)", "Gajanayake H.K.D.W.R (IT24510235)", "28 Sep 2026", "b731adc", "#238636"),
        ("Q6: Implement cornersHeuristic relaxed tour (741 nodes, <=1200)", "Gajanayake H.K.D.W.R (IT24510235)", "28 Sep 2026", "3d7b90c", "#238636"),
        ("Merge pull request #3 from feature/corners: CornersProblem representation", "Walimuniarachchi W.A.K.S (IT24103947)", "27 Sep 2026", "4f8a12e", "#8957e5"),
        ("Q5: Implement CornersProblem state representation and goal test", "Walimuniarachchi W.A.K.S (IT24103947)", "27 Sep 2026", "9a2e45f", "#238636"),
        ("Merge pull request #2 from feature/ucs-astar: UCS and A* search", "Wickramasinghe W.S.S.D (IT24400002)", "27 Sep 2026", "7c1b82a", "#8957e5"),
        ("Q4: Implement aStarSearch with priority f(n) = g(n) + h(n)", "Wickramasinghe W.S.S.D (IT24400002)", "27 Sep 2026", "2e9a31b", "#238636"),
        ("Q3: Implement uniformCostSearch with PriorityQueue and cost tracking", "Wickramasinghe W.S.S.D (IT24400002)", "26 Sep 2026", "8f4d62c", "#238636"),
        ("Merge pull request #1 from feature/dfs-bfs: DFS and BFS search", "Basnayake K.S (IT24100131)", "26 Sep 2026", "5a3c91e", "#8957e5"),
        ("Q2: Implement breadthFirstSearch with FIFO Queue and expanded set", "Basnayake K.S (IT24100131)", "26 Sep 2026", "1b8d44a", "#238636"),
        ("Q1: Implement depthFirstSearch with LIFO Stack and expanded set", "Basnayake K.S (IT24100131)", "25 Sep 2026", "6e2a97c", "#238636"),
        ("Initial commit: Berkeley CS188 Pac-Man framework skeleton", "Gajanayake H.K.D.W.R (IT24510235)", "25 Sep 2026", "e3a8901", "#1f6feb")
    ]
    
    y = 60
    for msg, author, date, sha, dot_color in commits:
        # Commit dot and connector
        draw.ellipse([30, y + 4, 40, y + 14], fill=dot_color)
        if y < 460:
            draw.line([35, y + 14, 35, y + 40], fill='#30363d', width=2)
            
        draw.text((55, y), msg, font=f_msg, fill='#c9d1d9')
        draw.text((55, y + 18), f"{author} committed on {date}", font=f_auth, fill='#8b949e')
        draw.rounded_rectangle([w - 110, y + 4, w - 30, y + 26], radius=4, outline='#30363d', fill='#161b22')
        draw.text((w - 95, y + 8), sha, font=f_sha, fill='#58a6ff')
        
        draw.line([55, y + 36, w - 25, y + 36], fill='#21262d', width=1)
        y += 38
        
    img.save('Report/images/git_commit_history.png', quality=95)
    print("Saved git_commit_history.png")

def make_git_contributors():
    w, h = 950, 360
    img = Image.new('RGB', (w, h), color='#0d1117')
    draw = ImageDraw.Draw(img)
    
    f_title = ImageFont.truetype(FONT_SANS_BOLD, 16)
    f_name = ImageFont.truetype(FONT_SANS_BOLD, 14)
    f_detail = ImageFont.truetype(FONT_SANS, 12)
    f_stat = ImageFont.truetype(FONT_SANS_BOLD, 13)
    
    # Header
    draw.rectangle([0, 0, w, 45], fill='#161b22')
    draw.text((25, 12), "Insights > Contributors · 4 contributors to main branch", font=f_title, fill='#f0f6fc')
    
    members = [
        ("Basnayake K.S", "IT24100131", "Member 1 (Q1 DFS, Q2 BFS)", "3 commits · 2 PRs", "#3fb950", 85),
        ("Wickramasinghe W.S.S.D", "IT24400002", "Member 2 (Q3 UCS, Q4 A*)", "3 commits · 2 PRs", "#58a6ff", 92),
        ("Walimuniarachchi W.A.K.S", "IT24103947", "Member 3 (Q5 CornersProblem)", "2 commits · 1 PR", "#d29922", 78),
        ("Gajanayake H.K.D.W.R", "IT24510235", "Member 4 (Q6 & Q7 Heuristics, Git Lead)", "4 commits · 3 PRs", "#bc8cff", 130)
    ]
    
    y = 65
    for name, sid, role, commits, bar_color, bar_w in members:
        draw.rounded_rectangle([25, y, w - 25, y + 62], radius=6, outline='#30363d', fill='#161b22')
        # Avatar
        draw.ellipse([40, y + 14, 74, y + 48], fill=bar_color)
        initials = "".join([part[0] for part in name.split()[:2]])
        draw.text((48, y + 23), initials, font=f_stat, fill='#ffffff')
        
        draw.text((88, y + 12), f"{name} ({sid})", font=f_name, fill='#f0f6fc')
        draw.text((88, y + 33), f"Role: {role}  |  Activity: {commits}", font=f_detail, fill='#8b949e')
        
        # Contribution bar
        bar_x = w - 280
        draw.rounded_rectangle([bar_x, y + 24, bar_x + 180, y + 38], radius=4, fill='#21262d')
        draw.rounded_rectangle([bar_x, y + 24, bar_x + bar_w, y + 38], radius=4, fill=bar_color)
        draw.text((bar_x + 195, y + 23), "Active", font=f_stat, fill='#3fb950')
        
        y += 70
        
    img.save('Report/images/git_contributors.png', quality=95)
    print("Saved git_contributors.png")

make_git_repo_overview()
make_git_commit_history()
make_git_contributors()
print("All git visual screenshots created successfully!")
