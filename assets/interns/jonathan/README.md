# 📘 Jonathan Gasaatura Internship Log

**Role:** High School Analyst Intern          
**Project:** Orioles Analytics Dashboard      
**Affiliation:** Ukubona LLC       
**Final Goal:** Class presentation showcasing full analytical pipeline and narrative insight      

---

## ✅ 1. Orientation & Progress Tracker

<details >
<summary>🗂️ Master Checklist</summary>

* [x] Onboarding: GitHub, web pages, and template setup
* [x] First website: content edits (text, images, `.html`)
* [ ] Setup local-to-remote GitHub workflow using VS Code
* [ ] Create and clean up a tidy working directory
* [ ] Introduce branching for collaborative repo management
* [ ] Confirm GitHub repo and folder structure are clean and complete
* [ ] Check that all visuals load and scale on desktop and mobile
* [ ] Verify HTML styling matches Ukubona brand standards
* [ ] Identify three core statistical claims in the project
* [ ] Prepare a 60-second summary of the project
* [ ] Draft and finalize the project’s opening statement for presentation

</details>

<details>
<summary>📅 Daily Log</summary>

### May 15, 2025

* [x] Finalized ESPN-style WhatsApp commentary layout
* [x] Updated OBP trend chart using synthetic game data
* [ ] Review OBP narrative: Is it more about pitch selection or poor Yankee shifts?
* [ ] Discuss first draft of presentation outline

### May 19, 2025

* [ ] Add pitch sequence whiff-rate chart for Grayson Rodriguez
* [ ] Write “Tactical Takeaways” in bullet form first, then expand to paragraph
* [ ] Run `git pull` / `git commit` / `git push` practice with local VS Code

### May 20, 2025

*(Add notes here...)*

</details>

---

## 🧠 2. Git Fluency: UI → Codespaces → VS Code → Local

<details open>
<summary>🌱 Manual Branching via GitHub UI (Starter Level)</summary>

* [x] Open the repo on GitHub in a browser.
* [ ] Click the 🔀 branch dropdown near `main`.
* [ ] Type a new name like `jonathan-notes` → **Create branch**.
* [ ] Click a file (e.g. `README.md`), make a small change.
* [ ] Commit directly to your new branch.
* [ ] Click **Compare & pull request** → Describe your work → **Create pull request**.

> 🧠 **Why this matters:** You just forked a path. No one else is touched. This is your test drive.

</details>

<details>
<summary>🧹 How to Delete a Git Branch</summary>

<details>
<summary>🗑️ 1. Delete a <strong>Local</strong> Branch (on your machine)</summary>

```bash
git branch -d my-branch       # only if merged
git branch -D my-branch       # force delete
```

✅ Works in:

* Codespaces terminal
* Local VS Code terminal

⚠️ This does **not** affect GitHub.

</details>

<details>
<summary>🌐 2. Delete a <strong>Remote</strong> Branch (on GitHub)</summary>

```bash
git push origin --delete my-branch
```

Removes the branch from GitHub. Useful after merge or cleanup.

</details>

<details>
<summary>🖱️ 3. Delete via GitHub Web UI</summary>

* Go to the **Branches** tab of your repo
* Find your branch, click the trash 🗑️ icon
* Or, if you just merged a PR, click **Delete branch** at the bottom of the PR page

</details>

<details>
<summary>💡 4. Pro Tips</summary>

```bash
git branch      # local
git branch -r   # remote
```

You can't delete a branch you're on! Run:

```bash
git checkout main
```

first.

</details>

</details>

<details>
<summary>💻 Codespaces: Terminal + Confidence</summary>

* [ ] Open Codespaces from GitHub (green **Code** button)
* [ ] Confirm your branch:

  ```bash
  git branch
  ```
* [ ] Delete your branch (after merge):

  ```bash
  git branch -d your-branch-name
  git push origin --delete your-branch-name
  ```

> 🧠 **Why this matters:** You now control the full lifecycle of a branch.

</details>

<details>
<summary>🧰 Local Git via VS Code (Pro-Level)</summary>

* [ ] Open Terminal on Mac
* [ ] Clone the repo:

  ```bash
  git clone git@github.com:YOUR_USERNAME/YOUR_REPO.git
  cd YOUR_REPO
  ```
* [ ] Create a branch:

  ```bash
  git checkout -b jonathan-notes
  ```
* [ ] Edit in VS Code
* [ ] Commit + push:

  ```bash
  git add .
  git commit -m "My edits"
  git push -u origin jonathan-notes
  ```

> 🧠 **Why this matters:** This is how real engineers work. You're now independent.

</details>

<details>
<summary>🐍 Bonus: Python Setup with venv</summary>

* [ ] Check Python:

  ```bash
  python3 --version
  ```
* [ ] Create environment:

  ```bash
  python3 -m venv myenv
  source myenv/bin/activate
  pip install -r requirements.txt
  ```

> 🧠 Use this for deploying scripts, notebooks, and data science pipelines.

</details>

---

## 🎯 3. Final Presentation Milestones

<details>
<summary>📊 Dossier & Countdown</summary>

### 📄 Profile

* **Name:** Jonathan Gasaatura
* **Grade:** High School Senior
* **Aspirations:** Sports Data Scientist → MLB Front Office Analyst
* **Skills (as of May 2025):**

  * Python (pandas, seaborn, matplotlib)
  * Statcast + Baseball-Reference
  * HTML/CSS, dashboarding
  * OBP curves, pitch sequence visuals
  * Multi-format storytelling (ESPN, WhatsApp, academic)

### ⏳ Countdown Timeline

| Day     | Focus               | Deliverable                                                     | Blockers                 | Mentor Action                          |
| ------- | ------------------- | --------------------------------------------------------------- | ------------------------ | -------------------------------------- |
| T–9     | Define thesis       | 3-sentence focus (OBP surge = plate discipline + shift failure) | Stat clarity             | Offer example thesis formats           |
| T–8     | Code audit          | One clean repo with data + README                               | Env issues               | Check Python pipeline + data structure |
| T–7     | Visualizations      | Add xwOBA + pitch sequence plots                                | Aesthetic clutter        | Chart simplification feedback          |
| T–6     | Writing begins      | 300 words: Grayson, Gunnar, OBP summary                         | Redundancy               | Editing pass + WhatsApp version        |
| T–5     | Wiki integration    | Add Camden + bullpen to Ukubona HTML                            | TOC formatting           | Check mobile + float layout            |
| T–4     | Mock presentation 1 | Live demo + slides                                              | Needs hook               | ESPN + Wilde-style dialogue injection  |
| T–3     | Peer review         | Record or share for peer feedback                               | Script dependence        | Emphasize verbal flow over reading     |
| T–2     | Polish              | Add favicon, mobile QA, chart labeling                          | Visual last-minute fixes | Run speed + link checks                |
| T–1     | Rehearsal           | Rehearse 2x + mock Q\&A                                         | Clock issues             | Simulate classroom pressure            |
| **T–0** | 🎤 Present          | Deliver project to class                                        | None                     | Celebrate + document                   |

</details>

---

> Tip: This single markdown file tracks learning, shows technical maturity, and builds a shareable portfolio. Jonathan can point to it as evidence of full-stack growth—technical, analytical, and communicative.
