# Git Homework Tasks Submission Report

**Student Name:** Srividya Ponnaganti  
**Course / Assignment:** DevOps - Git Homework Tasks  
**Date:** October 7, 2026  
**Repository Branch Structure:** `main`, `feature/service-modules`

---

## Table of Contents
1. [Task 1: `git commit -a -m` vs `git commit -m`](#task-1-git-commit--a--m-vs-git-commit--m)
   - [Core Concept & Differences](#11-core-concept--differences)
   - [Practical Demonstration & Terminal Outputs](#12-practical-demonstration--terminal-outputs)
   - [Key Takeaways](#13-key-takeaways)
2. [Task 2: Git Cherry-Pick](#task-2-git-cherry-pick)
   - [Concept & Use Cases](#21-concept--use-cases)
   - [Step 1: Commits in `main` Branch](#step-1-commits-in-main-branch)
   - [Step 2: Create New Branch & Make Commits](#step-2-create-new-branch--make-commits)
   - [Step 3: Identify Specific Commit using `git log`](#step-3-identify-specific-commit-using-git-log)
   - [Step 4: Cherry-Pick Target Commit to `main`](#step-4-cherry-pick-target-commit-to-main)
   - [Step 5: Verification & Inspection](#step-5-verification--inspection)
3. [Summary of Git Commands Used](#summary-of-git-commands-used)

---

## Task 1: `git commit -a -m` vs `git commit -m`

### 1.1 Core Concept & Differences

In Git, preparing changes to be saved into history involves two areas: the **Working Directory** and the **Staging Area (Index)**.

| Feature / Behavior | `git commit -m "message"` | `git commit -a -m "message"` |
| :--- | :--- | :--- |
| **Requires prior `git add`?** | **Yes**, only commits changes that are already staged in the Index. | **No** (for tracked files). Automatically stages and commits. |
| **Handles modified tracked files?** | Only if explicitly staged with `git add <file>`. | **Yes**, automatically stages and commits all modified tracked files. |
| **Handles deleted tracked files?** | Only if explicitly staged with `git add`/`git rm`. | **Yes**, automatically stages removals of tracked files. |
| **Handles brand new (untracked) files?** | **No**. Must run `git add <new_file>` first. | **No**. `-a` only affects already *tracked* files. Untracked files remain untouched. |
| **Primary Use Case** | Granular, intentional commits where only specific files or hunks should be committed. | Quick commits when all edits across existing project files should be saved together. |

---

### 1.2 Practical Demonstration & Terminal Outputs

#### Test A: Modifying a tracked file and running `git commit -m` without staging
1. We modified `sample.txt` (a tracked file).
2. We attempted to commit directly with `git commit -m`:

```bash
$ echo "Line 2: Modifying tracked file for git commit -m test" >> sample.txt
$ git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   sample.txt

no changes added to commit (use "git add" and/or "git commit -a")

$ git commit -m "Attempt to commit modified tracked file with only -m flag"
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   sample.txt

no changes added to commit (use "git add" and/or "git commit -a")
```
> **Observation:** The commit failed to record any changes because the modified file was not staged in the Git Index.

---

#### Test B: Using `git commit -a -m` on modified tracked files
1. With the unstaged changes still in `sample.txt`, we executed `git commit -a -m`:

```bash
$ git commit -a -m "Commit modified tracked file using git commit -a -m"
[main 11bf2b3] Commit modified tracked file using git commit -a -m
 1 file changed, 1 insertion(+)

$ git status
On branch main
nothing to commit, working tree clean
```
> **Observation:** `git commit -a -m` automatically detected the tracked modified file, staged it internally, and created the commit in a single operation.

---

#### Test C: Behavior of `git commit -a -m` with untracked (new) files
1. We created a brand new untracked file `untracked_file.txt` and modified `sample.txt`:

```bash
$ echo "Line 3: Another change in tracked file" >> sample.txt
$ echo "I am a brand new untracked file" > untracked_file.txt

$ git commit -a -m "Commit tracked changes while untracked file exists"
[main 5b6fc1d] Commit tracked changes while untracked file exists
 1 file changed, 1 insertion(+)

$ git status
On branch main
Untracked files:
  (use "git add <file>..." to include in what will be committed)
	untracked_file.txt

nothing added to commit but untracked files present (use "git add" to track)
```
> **Observation:** `git commit -a -m` committed the modifications in `sample.txt`, but completely ignored `untracked_file.txt`. Untracked files **always require an explicit `git add`**.

---

### 1.3 Key Takeaways
- `git commit -m` strictly respects the staging area.
- `git commit -a -m` is shorthand for `git add -u` (stage modified and deleted tracked files) followed by `git commit -m`.
- New files must always be tracked with `git add` at least once before `-a` can include them.

---

## Task 2: Git Cherry-Pick

### 2.1 Concept & Use Cases

`git cherry-pick <commit-hash>` is a powerful Git command that allows you to choose a specific commit from one branch and apply its exact changes onto your current working branch as a brand new commit.

#### Common Real-World Scenarios:
1. **Hotfixing Production:** Porting an urgent bug fix commit from a development/feature branch directly into `main`/`production` without releasing unfinished features.
2. **Extracting Shared Utilities:** Pulling a helpful helper function or module from an experimental branch into the main codebase.
3. **Selective Merging:** When a full branch merge or rebase would bring unwanted commits.

---

### Step 1: Commits in `main` Branch

We established the baseline repository history on `main`:

```bash
$ git log --oneline --graph --decorate
* 7156e5f (HEAD -> main) Add and commit newly tracked file explicitly
* 5b6fc1d Commit tracked changes while untracked file exists
* 11bf2b3 Commit modified tracked file using git commit -a -m
* b25020c Initial commit: Setup repo with README and sample file
```

---

### Step 2: Create New Branch & Make Commits

We created a feature branch named `feature/service-modules` and made 3 discrete commits:

```bash
$ git checkout -b feature/service-modules
Switched to a new branch 'feature/service-modules'

# Commit 1: Auth Service
$ git commit -m "feat(auth): Add user authentication service module"
[feature/service-modules 266c156] feat(auth): Add user authentication service module
 1 file changed, 3 insertions(+)
 create mode 100644 auth.py

# Commit 2: Calculator Utility (Target commit for cherry-pick)
$ git commit -m "feat(helpers): Add standalone calculator utility function"
[feature/service-modules 88d0851] feat(helpers): Add standalone calculator utility function
 1 file changed, 5 insertions(+)
 create mode 100644 helpers/calculator.py

# Commit 3: Payment Service
$ git commit -m "feat(payment): Add payment gateway processing service"
[feature/service-modules 9a60712] feat(payment): Add payment gateway processing service
 1 file changed, 3 insertions(+)
 create mode 100644 payment.py
```

---

### Step 3: Identify Specific Commit using `git log`

We inspected the commit log across all branches to locate the target commit hash:

```bash
$ git log --oneline --graph --all --decorate
* 9a60712 (HEAD -> feature/service-modules) feat(payment): Add payment gateway processing service
* 88d0851 feat(helpers): Add standalone calculator utility function
* 266c156 feat(auth): Add user authentication service module
* 7156e5f (main) Add and commit newly tracked file explicitly
* 5b6fc1d Commit tracked changes while untracked file exists
* 11bf2b3 Commit modified tracked file using git commit -a -m
* b25020c Initial commit: Setup repo with README and sample file
```

> **Target Commit Identified:**  
> **Hash:** `88d0851`  
> **Subject:** `feat(helpers): Add standalone calculator utility function`  
> **File:** `helpers/calculator.py`

---

### Step 4: Cherry-Pick Target Commit to `main`

1. Switch back to the `main` branch.
2. Run `git cherry-pick 88d0851`:

```bash
$ git checkout main
Switched to branch 'main'

$ git cherry-pick 88d0851
[main cfe3f3e] feat(helpers): Add standalone calculator utility function
 Date: Wed Oct 7 22:08:20 2026 +0530
 1 file changed, 5 insertions(+)
 create mode 100644 helpers/calculator.py
```

---

### Step 5: Verification & Inspection

#### A. Full Commit Tree Verification
```bash
$ git log --all --graph --oneline --decorate
* cfe3f3e (HEAD -> main) feat(helpers): Add standalone calculator utility function
| * 9a60712 (feature/service-modules) feat(payment): Add payment gateway processing service
| * 88d0851 feat(helpers): Add standalone calculator utility function
| * 266c156 feat(auth): Add user authentication service module
|/  
* 7156e5f Add and commit newly tracked file explicitly
* 5b6fc1d Commit tracked changes while untracked file exists
* 11bf2b3 Commit modified tracked file using git commit -a -m
* b25020c Initial commit: Setup repo with README and sample file
```

#### B. Working Tree & File Verification on `main`
```bash
$ ls -la
total 24
drwxr-xr-x  7 srividya  staff   224 Oct  7 22:08 .
drwxr-xr-x@ 13 srividya  staff   416 Oct  7 22:08 .git
-rw-r--r--@  1 srividya  staff    33 Oct  7 22:08 README.md
drwxr-xr-x@  3 srividya  staff    96 Oct  7 22:08 helpers
-rw-r--r--@  1 srividya  staff   125 Oct  7 22:08 sample.txt
-rw-r--r--@  1 srividya  staff    32 Oct  7 22:08 untracked_file.txt

$ ls helpers/
calculator.py

$ cat helpers/calculator.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
```

#### C. Isolation Check
- `helpers/calculator.py` is present on `main` branch.
- `auth.py` and `payment.py` are **NOT** present on `main` branch.
- This confirms that **only** the selected commit was incorporated into `main`.

---

## Summary of Git Commands Used

| Command | Purpose |
| :--- | :--- |
| `git init -b main` | Initialize a Git repository with `main` as the default branch |
| `git status` | Check working directory and staging area status |
| `git add <file>` | Stage a file to the Index |
| `git commit -m "<msg>"` | Commit staged changes with a message |
| `git commit -a -m "<msg>"` | Stage modified/deleted tracked files and commit in one step |
| `git log --oneline --graph --decorate --all` | Visualize commit history across all branches |
| `git checkout -b <branch>` | Create and switch to a new branch |
| `git checkout <branch>` | Switch to an existing branch |
| `git cherry-pick <hash>` | Apply changes from a specific commit onto the current branch |

---
*Report generated and verified in local Git workspace.*
