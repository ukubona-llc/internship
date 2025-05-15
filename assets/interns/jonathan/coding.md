
## ✅ Branching & Pushing Fluency Tracker

<details>
<summary>🌐 1. GitHub Web UI (Beginner)</summary>

- [ ] Open the repo in a browser
- [ ] Click the 🔀 branch dropdown near "main"
- [ ] Type new branch name (e.g. `jonathan-notes`) and hit **Create branch**
- [ ] Click a file to edit (e.g. `README.md`), make a change, and click **Commit changes**
- [ ] Commit directly to your new branch
- [ ] Click **Compare & pull request** to open a PR
- [ ] Add a description and click **Create pull request**
- [ ] (Optional) Merge it yourself, or wait for review

</details>

<details>
<summary>💻 2. GitHub Codespaces (Intermediate)</summary>

- [ ] Click the green **<> Code** button → "Open with Codespaces" → "New codespace"
- [ ] Open the built-in terminal (`Ctrl+`` or top menu → Terminal → New Terminal)
- [ ] Create and switch to a new branch:  
```bash
  git checkout -b jonathan-notes
````

* [ ] Make changes in files using the VS Code editor (left panel)
* [ ] Save changes, then commit in terminal:

  ```bash
  git add .
  git commit -m "Added my notes"
  ```
* [ ] Push the branch:

  ```bash
  git push -u origin jonathan-notes
  ```
* [ ] Go back to GitHub → Open a pull request from that branch

</details>

<details>
<summary>🧠 3. VS Code on Mac (Advanced)</summary>

* [ ] Confirm Git is installed:

  ```bash
  git --version
  ```

  If not:

  ```bash
  brew install git
  ```
* [ ] Clone the repo from GitHub:

  ```bash
  git clone git@github.com:YOUR_USERNAME/YOUR_REPO.git
  cd YOUR_REPO
  ```
* [ ] Create a new branch:

  ```bash
  git checkout -b jonathan-notes
  ```
* [ ] Make edits in VS Code
* [ ] Commit your changes:

  ```bash
  git add .
  git commit -m "My local updates"
  ```
* [ ] Push your branch:

  ```bash
  git push -u origin jonathan-notes
  ```
* [ ] Create a pull request via GitHub

</details>

<details>
<summary>🐍 (Optional) Python Setup with venv</summary>

> For working with Jupyter Books or Python-powered deploy scripts

* [ ] Install Python (if needed):

  ```bash
  brew install python
  ```
* [ ] Create a virtual environment:

  ```bash
  python3 -m venv myenv
  source myenv/bin/activate
  ```
* [ ] Install dependencies:

  ```bash
  pip install -r requirements.txt
  ```
* [ ] Run build or deploy scripts:

  ```bash
  python deploy.py
  ```

</details>

---

**🧭 Pro Tip:** Always double check which branch you're on:

```bash
git branch
```

If you're not on the right one:

```bash
git checkout your-branch-name
```

