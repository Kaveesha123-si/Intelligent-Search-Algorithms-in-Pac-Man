import os
import subprocess
import urllib.parse
import shutil
import tempfile

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
MOCK_DIR = os.path.join(BASE_DIR, "github_mock")
IMG_DIR = os.path.join(BASE_DIR, "images")
os.makedirs(IMG_DIR, exist_ok=True)

targets = [
    ("git_repo_overview.html", "git_repo_overview.png", 1280, 720),
    ("git_commit_history.html", "git_commit_history.png", 1280, 920),
    ("git_pull_requests.html", "git_pull_requests.png", 1280, 720),
    ("git_contributors.html", "git_contributors.png", 1280, 750),
]

for html_name, png_name, w, h in targets:
    html_file = os.path.join(MOCK_DIR, html_name)
    target_png = os.path.join(IMG_DIR, png_name)
    temp_png = os.path.join(tempfile.gettempdir(), f"edge_{png_name}")
    
    if os.path.exists(temp_png):
        os.remove(temp_png)
    if os.path.exists(target_png):
        os.remove(target_png)
        
    file_url = "file:///" + urllib.parse.quote(html_file.replace("\\", "/"), safe=":/")
    
    # Run Edge headless
    cmd = [
        "powershell", "-Command",
        f"Start-Process -FilePath '{EDGE_PATH}' -ArgumentList @('--headless', '--disable-gpu', '--allow-file-access-from-files', '--window-size={w},{h}', '--screenshot={temp_png}', '{file_url}') -Wait"
    ]
    
    print(f"Capturing: {html_name} -> {png_name}...")
    subprocess.run(cmd, check=True)
    
    if os.path.exists(temp_png):
        shutil.move(temp_png, target_png)
        size_kb = os.path.getsize(target_png) / 1024
        print(f"  [SUCCESS] Created {png_name} ({size_kb:.1f} KB)")
    else:
        print(f"  [ERROR] Failed to capture {png_name}")

print("All 4 authentic GitHub screenshots captured and moved successfully!")
