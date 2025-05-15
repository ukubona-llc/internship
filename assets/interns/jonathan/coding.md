

## ✅ Git Branching & Pushing Fluency Tracker

<details open>
<summary>🌱 1. Manual Branching via GitHub UI (Starter Level)</summary>

Start by *making your own lane*.

* [x] Open the repo on GitHub in a browser.
* [x] Click the 🔀 branch dropdown near `main`.
* [x] Type a new name like `jonathan-notes` → **Create branch**.
* [x] Click a file (e.g. `README.md`), make a small change.
* [x] Commit directly to your new branch.
* [x] Click **Compare & pull request** → Describe your work → **Create pull request**.

> 🧠 **Why this matters:** You just forked a path. No one else is touched. This is your test drive.

</details>

<details>
<summary>🧹 2. Can't delete that branch? Time to level up (Codespaces)</summary>

GitHub UI can **create** branches—but not **delete** them. This is your invitation to **Codespaces**.

* [ ] Click the green **<> Code** button → “Open with Codespaces” → New codespace.

* [ ] In the terminal, confirm you're on your branch:

  ```bash
  git branch
  ```

* [ ] To delete your branch (after it's merged):

  ```bash
  git branch -d jonathan-notes
  git push origin --delete jonathan-notes
  ```

> 🧠 **Why this matters:** You now control the lifecycle of a branch—birth *and* death.

</details>

<details>
<summary>🧠 3. Local Git (VS Code on Mac – Real-World Dev)</summary>

Now you're ready for full autonomy:

* [ ] Open Terminal on your Mac.

* [ ] Clone the repo:

  ```bash
  git clone git@github.com:YOUR_USERNAME/YOUR_REPO.git
  cd YOUR_REPO
  ```

* [ ] Make a new branch:

  ```bash
  git checkout -b jonathan-notes
  ```

* [ ] Edit in VS Code. Save.

* [ ] Commit and push:

  ```bash
  git add .
  git commit -m "My local edits"
  git push -u origin jonathan-notes
  ```

* [ ] Open your pull request on GitHub.

> 🧠 **Why this matters:** This is real. It’s how professionals ship code. You can now work offline, push when ready, and handle conflicts like a grown-up.

</details>

<details>
<summary>🐍 4. (Bonus) Python Setup with `venv`</summary>

If your repo uses Python (e.g. Jupyter Books, deploy scripts):

* [ ] Check if Python is installed:

  ```bash
  python3 --version
  ```

* [ ] Set up your environment:

  ```bash
  python3 -m venv myenv
  source myenv/bin/activate
  pip install -r requirements.txt
  ```

> 🧠 **Why this matters:** One day you'll want to test your scripts in isolation. This gives you clean rooms for clean experiments.

</details>

---

## 🔁 Daily Drill

Every day, ask:

```bash
git branch        # Where am I?
git status        # What changed?
```

Then *act accordingly*.
 
