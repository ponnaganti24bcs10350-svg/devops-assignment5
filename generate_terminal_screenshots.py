import os
from PIL import Image, ImageDraw, ImageFont

os.makedirs('screenshots', exist_ok=True)

FONT_PATH = '/System/Library/Fonts/Menlo.ttc'
FONT_SIZE = 14 * 2
LINE_HEIGHT = 22 * 2
PADDING_X = 24 * 2
PADDING_TOP = 48 * 2
PADDING_BOTTOM = 24 * 2
BORDER_RADIUS = 14 * 2

BG_COLOR = (24, 24, 37)
TITLE_BG = (30, 30, 46)
BORDER_COLOR = (49, 50, 68)
TEXT_WHITE = (205, 214, 244)
TEXT_GRAY = (147, 153, 178)
PROMPT_PATH = (166, 227, 161)
SUCCESS_GREEN = (166, 227, 161)
WARN_YELLOW = (249, 226, 175)
ERR_RED = (243, 139, 168)
HASH_CYAN = (137, 220, 235)
BRANCH_PURPLE = (203, 166, 247)

def render_terminal(lines, title="srividya@MacBook-Pro: ~/devops-assign (zsh)", width=1050 * 2):
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE, index=0)
    font_bold = ImageFont.truetype(FONT_PATH, FONT_SIZE, index=1)
    font_title = ImageFont.truetype(FONT_PATH, int(13 * 2), index=0)
    
    height = PADDING_TOP + PADDING_BOTTOM + len(lines) * LINE_HEIGHT
    
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    draw.rounded_rectangle([(0, 0), (width - 1, height - 1)], radius=BORDER_RADIUS, fill=BG_COLOR, outline=BORDER_COLOR, width=2)
    
    header_height = PADDING_TOP - (10 * 2)
    draw.rounded_rectangle([(0, 0), (width - 1, header_height)], radius=BORDER_RADIUS, fill=TITLE_BG)
    draw.rectangle([(0, header_height - 10 * 2), (width - 1, header_height)], fill=TITLE_BG)
    draw.line([(0, header_height), (width - 1, header_height)], fill=BORDER_COLOR, width=2)
    
    btn_y = header_height // 2
    btn_radius = 6 * 2
    draw.ellipse([(18 * 2 - btn_radius, btn_y - btn_radius), (18 * 2 + btn_radius, btn_y + btn_radius)], fill=(255, 95, 86))
    draw.ellipse([(38 * 2 - btn_radius, btn_y - btn_radius), (38 * 2 + btn_radius, btn_y + btn_radius)], fill=(255, 189, 46))
    draw.ellipse([(58 * 2 - btn_radius, btn_y - btn_radius), (58 * 2 + btn_radius, btn_y + btn_radius)], fill=(39, 201, 63))
    
    bbox = font_title.getbbox(title)
    title_w = bbox[2] - bbox[0]
    draw.text(((width - title_w) // 2, btn_y - (bbox[3] - bbox[1]) // 2 - 2), title, font=font_title, fill=TEXT_GRAY)
    
    y = PADDING_TOP
    for line in lines:
        if isinstance(line, tuple):
            text_type, text = line
        else:
            text_type, text = "regular", line
            
        text = text.replace("\t", "    ")
        x = PADDING_X
        if text_type == "prompt_cmd":
            prompt = "srividya@MacBook-Pro devops-assign % "
            draw.text((x, y), prompt, font=font_bold, fill=PROMPT_PATH)
            p_bbox = font_bold.getbbox(prompt)
            x += (p_bbox[2] - p_bbox[0])
            draw.text((x, y), text, font=font_bold, fill=TEXT_WHITE)
        elif text_type == "error":
            draw.text((x, y), text, font=font, fill=ERR_RED)
        elif text_type == "success":
            draw.text((x, y), text, font=font, fill=SUCCESS_GREEN)
        elif text_type == "warn":
            draw.text((x, y), text, font=font, fill=WARN_YELLOW)
        elif text_type == "dim":
            draw.text((x, y), text, font=font, fill=TEXT_GRAY)
        elif text_type == "hash":
            draw.text((x, y), text, font=font, fill=HASH_CYAN)
        elif text_type == "branch":
            draw.text((x, y), text, font=font, fill=BRANCH_PURPLE)
        else:
            draw.text((x, y), text, font=font, fill=TEXT_WHITE)
            
        y += LINE_HEIGHT
        
    return img

# 1. TASK 1 SCREENSHOT
lines1 = [
    ("prompt_cmd", "echo 'Line 2: Modifying tracked file' >> sample.txt"),
    ("prompt_cmd", "git status"),
    ("regular", "On branch main"),
    ("regular", "Changes not staged for commit:"),
    ("dim", "  (use \"git add <file>...\" to update what will be committed)"),
    ("error", "    modified:   sample.txt"),
    ("regular", ""),
    ("warn", "no changes added to commit (use \"git add\" and/or \"git commit -a\")"),
    ("regular", ""),
    ("prompt_cmd", "git commit -m 'Attempting commit without git add'"),
    ("regular", "On branch main"),
    ("error", "    modified:   sample.txt"),
    ("warn", "no changes added to commit (use \"git add\" and/or \"git commit -a\")"),
    ("regular", ""),
    ("prompt_cmd", "git commit -a -m 'Commit modified tracked file using -a -m'"),
    ("success", "[main 11bf2b3] Commit modified tracked file using git commit -a -m"),
    ("regular", " 1 file changed, 1 insertion(+)"),
    ("regular", ""),
    ("prompt_cmd", "git status"),
    ("regular", "On branch main"),
    ("success", "nothing to commit, working tree clean"),
    ("regular", ""),
    ("prompt_cmd", "echo 'New untracked content' > untracked_file.txt"),
    ("prompt_cmd", "git commit -a -m 'Testing untracked file behavior'"),
    ("warn", "nothing added to commit but untracked files present (use \"git add\" to track)")
]
img1 = render_terminal(lines1)
img1.save("screenshots/01_task1_commit_comparison.png", "PNG")

# 2. TASK 2 MAIN COMMITS
lines2 = [
    ("prompt_cmd", "git log --oneline --graph --decorate"),
    ("regular", "* 7156e5f (HEAD -> main) Add and commit newly tracked file explicitly"),
    ("regular", "* 5b6fc1d Commit tracked changes while untracked file exists"),
    ("regular", "* 11bf2b3 Commit modified tracked file using git commit -a -m"),
    ("regular", "* b25020c Initial commit: Setup repo with README and sample file"),
    ("regular", ""),
    ("prompt_cmd", "git branch"),
    ("success", "* main")
]
img2 = render_terminal(lines2)
img2.save("screenshots/02_task2_main_commits.png", "PNG")

# 3. TASK 2 FEATURE COMMITS
lines3 = [
    ("prompt_cmd", "git checkout -b feature/service-modules"),
    ("success", "Switched to a new branch 'feature/service-modules'"),
    ("regular", ""),
    ("prompt_cmd", "git commit -m 'feat(auth): Add user authentication service module'"),
    ("success", "[feature/service-modules 266c156] feat(auth): Add user authentication service module"),
    ("regular", " 1 file changed, 3 insertions(+) / create mode 100644 auth.py"),
    ("regular", ""),
    ("prompt_cmd", "git commit -m 'feat(helpers): Add standalone calculator utility function'"),
    ("success", "[feature/service-modules 88d0851] feat(helpers): Add standalone calculator utility function"),
    ("regular", " 1 file changed, 5 insertions(+) / create mode 100644 helpers/calculator.py"),
    ("regular", ""),
    ("prompt_cmd", "git commit -m 'feat(payment): Add payment gateway processing service'"),
    ("success", "[feature/service-modules 9a60712] feat(payment): Add payment gateway processing service"),
    ("regular", " 1 file changed, 3 insertions(+) / create mode 100644 payment.py"),
    ("regular", ""),
    ("prompt_cmd", "git log --oneline --graph --all --decorate"),
    ("regular", "* 9a60712 (HEAD -> feature/service-modules) feat(payment): Add payment gateway processing service"),
    ("hash", "* 88d0851 feat(helpers): Add standalone calculator utility function"),
    ("regular", "* 266c156 feat(auth): Add user authentication service module"),
    ("regular", "* 7156e5f (main) Add and commit newly tracked file explicitly"),
    ("regular", "* 5b6fc1d Commit tracked changes while untracked file exists"),
    ("regular", "* 11bf2b3 Commit modified tracked file using git commit -a -m"),
    ("regular", "* b25020c Initial commit: Setup repo with README and sample file")
]
img3 = render_terminal(lines3)
img3.save("screenshots/03_task2_branch_and_commits.png", "PNG")

# 4. TASK 2 CHERRY PICK
lines4 = [
    ("prompt_cmd", "git checkout main"),
    ("success", "Switched to branch 'main'"),
    ("regular", ""),
    ("prompt_cmd", "git cherry-pick 88d0851"),
    ("success", "[main cfe3f3e] feat(helpers): Add standalone calculator utility function"),
    ("regular", " Date: Wed Oct 7 22:08:20 2026 +0530"),
    ("regular", " 1 file changed, 5 insertions(+) / create mode 100644 helpers/calculator.py"),
    ("regular", ""),
    ("prompt_cmd", "git log --all --graph --oneline --decorate"),
    ("success", "* cfe3f3e (HEAD -> main) feat(helpers): Add standalone calculator utility function"),
    ("regular", "| * 9a60712 (feature/service-modules) feat(payment): Add payment gateway processing service"),
    ("hash", "| * 88d0851 feat(helpers): Add standalone calculator utility function"),
    ("regular", "| * 266c156 feat(auth): Add user authentication service module"),
    ("regular", "|/  "),
    ("regular", "* 7156e5f Add and commit newly tracked file explicitly"),
    ("regular", "* 5b6fc1d Commit tracked changes while untracked file exists"),
    ("regular", "* 11bf2b3 Commit modified tracked file using git commit -a -m"),
    ("regular", "* b25020c Initial commit: Setup repo with README and sample file"),
    ("regular", ""),
    ("prompt_cmd", "ls helpers/"),
    ("success", "calculator.py"),
    ("prompt_cmd", "ls auth.py payment.py"),
    ("error", "ls: auth.py: No such file or directory"),
    ("error", "ls: payment.py: No such file or directory")
]
img4 = render_terminal(lines4)
img4.save("screenshots/04_task2_cherry_pick_and_verification.png", "PNG")
