---
name: Trial
description: Push code to a GitHub repository. Use when the user wants to commit and push their code changes to GitHub. Stages all files, prompts for a commit message, and pushes to the main branch.
---

# GitHub Push Skill

Pushes the user's code to GitHub by running the full sequence: stage all files → commit → push. Never skip or reorder these steps.

## Workflow

### Step 1: Verify Git Repository

Run:

```bash
git remote -v
```

- If no remote is configured, ask the user for the GitHub repo URL and run:
  ```bash
  git remote add origin <url>
  ```
- If not a git repo at all, tell the user and stop.

### Step 2: Stage All Files

**Always run this. Never skip it.**

```bash
git add .
```

Then check what was staged:

```bash
git diff --cached --stat
```

- If the output is empty, tell the user: "There are no changes to commit." and stop.
- If there are staged changes, show them to the user and continue.

### Step 3: Ask for Commit Message

Ask the user exactly this:

> "What would you like your commit message to be?"

**Do not proceed until the user replies. Do not auto-generate a message.**

### Step 4: Commit and Push in One Sequence

Once the user provides a commit message, run these two commands back to back without stopping:

```bash
git commit -m "<user's commit message>"
git push origin main
```

**Do not run `git push` alone. Always run `git commit` first.**

If the branch is named `master` instead of `main`, use `master`.

If the push fails because the remote has new changes, run:

```bash
git pull origin main --rebase
git push origin main
```

### Step 5: Confirm Success

Show the user the output and confirm:

> "✅ Done! Your code has been committed and pushed to GitHub."

Include the commit hash from the output.

## Error Handling

- **Authentication error**: Tell the user to check their SSH key or GitHub personal access token.
- **Merge conflict**: Tell the user there are conflicts to resolve manually before pushing.
- **Nothing to commit**: Caught in Step 2 — tell the user and stop gracefully.