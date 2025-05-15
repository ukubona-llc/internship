 
 
## 🧹 How to Delete a Git Branch

<details>
<summary>🗑️ 1. Delete a <strong>Local</strong> Branch (on your machine)</summary>

- Only works if the branch is **merged**:
```bash
  git branch -d my-branch
````

* If it's **not merged**, and you're sure:

  ```bash
  git branch -D my-branch
  ```

* ✅ Works in:

  * Codespaces terminal
  * Local VS Code terminal

* ⚠️ Does **not** affect GitHub or anyone else’s copy.

</details>

<details>
<summary>🌐 2. Delete a <strong>Remote</strong> Branch (on GitHub)</summary>

* Run this from terminal (Codespaces or local):

  ```bash
  git push origin --delete my-branch
  ```

* This removes the branch from **GitHub itself**.

* Useful after merging or if a stale branch is no longer needed.

</details>

<details>
<summary>🖱️ 3. Delete via GitHub Web UI</summary>

* Navigate to your GitHub repo.
* Click **Branches** tab (usually just above file list).
* Find your branch in the list.
* Click the trash 🗑️ icon to delete it.

**OR**, if you just merged a pull request:

* Scroll to the bottom of the PR page.
* Click the gray button: **“Delete branch”**.

</details>

<details>
<summary>💡 4. Pro Tips</summary>

* Always check which branches are live:

  ```bash
  git branch        # local branches
  git branch -r     # remote branches
  ```

* Use:

  ```bash
  git checkout main
  ```

  before deleting, so you’re **not on** the branch you’re removing.

* You can’t delete the branch you’re currently using!

* Deleting stale branches keeps your repo clean and your brain fresher.

</details>
 
 
