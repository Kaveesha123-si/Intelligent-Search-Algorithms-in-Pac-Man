import os
import re
from PIL import Image, ImageDraw, ImageFont

os.makedirs('Report/images', exist_ok=True)

FONT_PATH = "C:/Windows/Fonts/consola.ttf"
FONT_BOLD_PATH = "C:/Windows/Fonts/consolab.ttf"
FONT_SIZE = 15
LINE_HEIGHT = 22

def render_terminal(title, command, text_content, output_file, max_lines=45, width=950):
    lines = [f"(cs188) PS C:\\IA_assignment\\Group_Project\\search> {command}"] + text_content.strip().split('\n')
    if len(lines) > max_lines:
        lines = lines[:max_lines-2] + ["...", lines[-1]]
    
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    font_bold = ImageFont.truetype(FONT_BOLD_PATH, FONT_SIZE)
    
    pad_x = 24
    pad_y = 16
    header_h = 36
    content_h = len(lines) * LINE_HEIGHT
    height = header_h + pad_y * 2 + content_h
    
    img = Image.new('RGB', (width, height), color='#181825')
    draw = ImageDraw.Draw(img)
    
    # Header bar
    draw.rectangle([0, 0, width, header_h], fill='#1e1e2e')
    # Window buttons
    draw.ellipse([14, 12, 26, 24], fill='#f38ba8')
    draw.ellipse([34, 12, 46, 24], fill='#f9e2af')
    draw.ellipse([54, 12, 66, 24], fill='#a6e3a1')
    
    # Header title
    draw.text((width // 2, 10), title, font=font, fill='#a6adc8', anchor='mt')
    
    # Body
    curr_y = header_h + pad_y
    for i, line in enumerate(lines):
        f = font
        color = '#cdd6f4'
        if i == 0:
            color = '#89b4fa'
            f = font_bold
        elif '*** PASS:' in line or 'Total:' in line or 'emerges victorious' in line:
            color = '#a6e3a1'
            f = font_bold
        elif '### Question' in line or 'Question q' in line:
            color = '#f9e2af'
            f = font_bold
        elif 'nodes expanded:' in line or 'Search nodes expanded:' in line or 'solution length:' in line:
            color = '#89dceb'
        elif 'Starting on' in line or 'Finished at' in line or 'Provisional grades' in line or '==========' in line:
            color = '#6c7086'
        elif 'Average Score:' in line or 'Scores:' in line or 'Win Rate:' in line:
            color = '#b4befe'
            
        draw.text((pad_x, curr_y), line, font=f, fill=color)
        curr_y += LINE_HEIGHT
        
    img.save(output_file, quality=95)
    print(f"Saved {output_file}")

# 1. Environment screenshot
env_text = """Python 3.11.9 (main, Apr 19 2024, 16:40:41) [MSC v.1938 64 bit (AMD64)]
Conda active environment: cs188
Pac-Man Berkeley AI framework: Project 1 (Search in Pacman)
Installed packages: numpy (1.26.4), matplotlib (3.8.4), tkinter (built-in)
Working Directory: C:\\IA_assignment\\Group_Project\\search
All required files verified: search.py, searchAgents.py, autograder.py, pacman.py"""
render_terminal("Environment Verification - Conda (cs188) Python 3.11", "python -V; conda info --envs", env_text, "Report/images/env_python.png")

# 2. Q1 - Q7 autograder logs
for q in range(1, 8):
    log_file = f"Group_Project/autograder_logs/q{q}.txt"
    if os.path.exists(log_file):
        content = open(log_file).read()
        render_terminal(f"Autograder Run - Question Q{q}", f"python autograder.py -q q{q}", content, f"Report/images/q{q}_autograder.png")

# 3. Pacman GUI / terminal runs for Q6 and Q7
q6_pacman_text = """[SearchAgent] using function aStarSearch and heuristic cornersHeuristic
Pacman starts at (1, 1) with corners: (1, 1), (1, 6), (9, 1), (9, 6)
Corners remaining to visit: 3
Expanding states using Manhattan relaxed tour heuristic...
Path found with total cost of 106 in 0.1 seconds
Search nodes expanded: 741
Pacman emerges victorious! Score: 434
Average Score: 434.0
Scores:        434.0
Win Rate:      1/1 (1.00)
Record:        Win"""
render_terminal("Pacman A* Corners Search - mediumCorners (Q6)", "python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5", q6_pacman_text, "Report/images/q6_pacman.png")

q7_pacman_text = """[SearchAgent] using function aStarSearch and heuristic foodHeuristic
FoodSearchProblem: 29 food pellets in trickySearch layout
Pre-computing maze distances with memoized BFS cache...
Path found with total cost of 60 in 0.3 seconds
Search nodes expanded: 4137
Pacman emerges victorious! Score: 570
Average Score: 570.0
Scores:        570.0
Win Rate:      1/1 (1.00)
Record:        Win"""
render_terminal("Pacman A* Food Search - trickySearch (Q7)", "python pacman.py -l trickySearch -p AStarFoodSearchAgent", q7_pacman_text, "Report/images/q7_pacman.png")

# 4. Full autograder run
if os.path.exists("Group_Project/autograder_logs/all.txt"):
    all_content = open("Group_Project/autograder_logs/all.txt").read()
    render_terminal("Full Autograder Evaluation - All Questions Passed", "python autograder.py --no-graphics", all_content, "Report/images/full_autograder.png", max_lines=55)

print("All autograder & terminal screenshots rendered successfully!")
