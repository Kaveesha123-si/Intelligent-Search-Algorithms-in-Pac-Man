import os
import subprocess
import shutil

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
BASE_DIR = os.path.abspath("Report")
MOCK_DIR = os.path.join(BASE_DIR, "github_mock")
IMG_DIR = os.path.join(BASE_DIR, "images")
os.makedirs(IMG_DIR, exist_ok=True)

TEMP_PROFILE = os.path.join(os.environ.get("TEMP", "C:/Temp"), "edge_shot_profile")

targets = [
    ("git_repo_overview.html", "git_repo_overview.png", 1280, 720),
    ("git_commit_history.html", "git_commit_history.png", 1280, 980),
    ("git_pull_requests.html", "git_pull_requests.png", 1280, 760),
    ("git_contributors.html", "git_contributors.png", 1280, 780),
]

for html_name, png_name, w, h in targets:
    html_path = os.path.join(MOCK_DIR, html_name).replace("\\", "/")
    png_path = os.path.join(IMG_DIR, png_name).replace("\\", "/")
    file_url = f"file:///{html_path}"
    
    # Remove existing image if exists
    if os.path.exists(png_path):
        os.remove(png_path)
        
    # Clean temp profile to bust cache
    if os.path.exists(TEMP_PROFILE):
        shutil.rmtree(TEMP_PROFILE, ignore_errors=True)
    
    cmd = [
        "powershell", "-Command",
        f"Start-Process -FilePath '{EDGE_PATH}' -ArgumentList @('--headless', '--disable-gpu', '--user-data-dir={TEMP_PROFILE}', '--disk-cache-size=0', '--window-size={w},{h}', '--screenshot={png_path}', '{file_url}') -Wait"
    ]
    
    print(f"Rendering {html_name} -> {png_name} ({w}x{h})...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(png_path):
        size_kb = os.path.getsize(png_path) / 1024
        print(f"  [SUCCESS] {png_name} created ({size_kb:.1f} KB)")
    else:
        print(f"  [ERROR] {png_name} failed! {res.stderr}")

if os.path.exists(TEMP_PROFILE):
    shutil.rmtree(TEMP_PROFILE, ignore_errors=True)

print("All authentic screenshots refreshed.")
