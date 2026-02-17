---
name: Trial
description: Push code to a GitHub repository. Use when the user wants to commit and push their code changes to GitHub. Stages all files, prompts for a commit message, and pushes to the main branch.
---

# GitHub Push Skill

Pushes the user's code to a GitHub repository by staging all changes, committing with a user-provided message, and pushing to the main branch.

## Workflow

Follow these steps in order:

### Step 1: Verify Git Repository

Check that the current directory is a git repository and has a remote configured:

```bash
git status
git remote -v
```

- If not a git repo, tell the user and stop.
- If no remote is configured, ask the user for the GitHub repo URL and run:
  ```bash
  git remote add origin <url>
  ```

### Step 2: Stage All Files

**Always run this command first, before checking status:**

```bash
git add .
```

Then show the user what was staged:

```bash
git diff --cached --stat
```

If the output is empty, tell the user there are no changes to commit and stop. Otherwise continue to Step 3.

### Step 3: Ask for Commit Message

Ask the user:

> "What would you like your commit message to be?"

Wait for their response before proceeding. Do not auto-generate a commit message — always ask.

### Step 4: Commit

Once the user provides a commit message, commit the staged changes:

```bash
git commit -m "<user's commit message>"
```

### Step 5: Push to Main

Push to the main branch:

```bash
git push origin main
```

- If the push fails because the remote has changes the local doesn't have, offer to pull first:
  ```bash
  git pull origin main --rebase
  git push origin main
  ```
- If the branch is `master` instead of `main`, use `master`.

### Step 6: Confirm Success

After a successful push, confirm to the user:

> "✅ Your code has been pushed to GitHub successfully!"

Show the commit hash and branch name from the output.

## Error Handling

- **Authentication errors**: Tell the user their GitHub credentials may need to be configured, and suggest checking their SSH key or personal access token.
- **Merge conflicts**: Tell the user there are conflicts that need to be resolved manually before pushing.
- **Nothing to commit**: Let the user know there are no changes to push.