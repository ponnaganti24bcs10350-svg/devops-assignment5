# Git Homework Assignment

**Name:** Srividya Ponnaganti  
**GitHub Repo:** https://github.com/ponnaganti24bcs10350-svg/devops-assignment5  

---

## Task 1: Understanding `git commit -a -m` vs `git commit -m`

### The Difference
- `git commit -m "message"`: Only commits changes that I have manually added to the staging area with `git add`.
- `git commit -a -m "message"`: Automatically stages all modified and deleted files that Git is already tracking and commits them in one step. It does not stage new untracked files.

### Testing and Output
I tested both commands in the terminal:
1. I modified an existing tracked file (`sample.txt`) and tried running `git commit -m`. Git refused to commit because the changes were not staged.
2. Next, I ran `git commit -a -m`. Git automatically staged the modified file and committed it cleanly.
3. Finally, I created a brand new file (`untracked_file.txt`) and tested `git commit -a -m`. The untracked file was ignored, proving that `-a` only works on already tracked files.

![Task 1 Terminal Output](screenshots/01_task1_commit_comparison.png)

---

## Task 2: Git Cherry-Pick

### Step 1: Base commits on `main` branch
I made initial commits on the `main` branch and checked the history using `git log`.

![Task 2 Main Commits](screenshots/02_task2_main_commits.png)

---

### Step 2: Create a new branch and add commits
I created a new branch named `feature/service-modules` using:
```bash
git checkout -b feature/service-modules
```
Then I made 3 commits:
1. `auth.py`
2. `helpers/calculator.py`
3. `payment.py`

I ran `git log --oneline --graph --all` to view the commits across branches. I identified the commit hash for the calculator helper (`88d0851`).

![Task 2 Feature Branch Commits](screenshots/03_task2_branch_and_commits.png)

---

### Step 3: Cherry-pick the commit into `main` and verify
1. I switched back to the `main` branch:
   ```bash
   git checkout main
   ```
2. I cherry-picked the calculator commit:
   ```bash
   git cherry-pick 88d0851
   ```
3. I checked `git log` and verified the files. The calculator file (`helpers/calculator.py`) is now in `main`, but `auth.py` and `payment.py` remain only on the feature branch.

![Task 2 Cherry Pick and Verification](screenshots/04_task2_cherry_pick_and_verification.png)

---

## Git Commands Used
- `git status`
- `git add <file>`
- `git commit -m "<message>"`
- `git commit -a -m "<message>"`
- `git log --oneline --graph --decorate --all`
- `git checkout -b <branch>`
- `git checkout <branch>`
- `git cherry-pick <commit-hash>`
