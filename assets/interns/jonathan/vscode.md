 
## 🧠 Ukubona Intern Setup Guide (Mac)

> *“From zero to `git push` in 10 minutes.”*

---

### 🚨 TL;DR — Git on Mac = Xcode Bottleneck

Git on Mac is crippled out-of-the-box. It’s *not standalone*. It lives **inside** Apple’s **Command Line Tools (CLT)**—installed via:

```bash
xcode-select --install
```

This is the **first and worst** bottleneck:

* No progress bar.
* No ETA.
* No escape if the popup breaks.

👉 **Don’t wait. Don’t wonder. Skip Apple.**

---

### ✅ Fastest Path: Homebrew Git (Bypass Apple)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install git
```

Now check:

```bash
git --version
which git  # should point to /opt/homebrew/bin/git
```

If you still see `/usr/bin/git`, you're stuck on the Apple leash.

---

## 💻 VS Code Setup (Intern Blitz – 10 min)

### 1. **Install VS Code**

* [https://code.visualstudio.com](https://code.visualstudio.com)
* Drag to Applications.

### 2. **Launch & Configure**

* Open VS Code → allow system prompts.
* Go to Extensions:

  * ✅ Python
  * ✅ Prettier
  * ✅ GitHub Copilot (optional)

### 3. **Create Folder + Test File**

```bash
mkdir ~/Desktop/intern-project
cd ~/Desktop/intern-project
code .
```

Inside VS Code:

* Create `test.py`:

```python
print("Hello, Ukubona!")
```

* Run ▶️ (install interpreter if prompted)

---

## 🚀 Git Push Workflow (From Local → GitHub)

### ❓ Ask: “Do you have a GitHub account?”

If not: [github.com](https://github.com) → 2-min signup + email verification.

### 🔧 Terminal Setup

```bash
git config --global user.name "Jonathan Gasaatura"
git config --global user.email "jonathan@example.com"
```

Create a repo online (public, no README).

Then:

```bash
cd ~/Desktop/intern-project
git init
git add index.html
git commit -m "First commit"
git remote add origin https://github.com/USERNAME/intern-project.git
git branch -M main
git push -u origin main
```

🎉 Done. Refresh browser → code is live.

---

## 🧪 Bonus: Sanity Check for Git + Python

```bash
git --version
which git         # Good = /opt/homebrew/bin/git
python3 --version # Should not be 2.x
which python3
```

---

## 🧱 Optional Add-Ons

* **Install Python** cleanly via Homebrew:

  ```bash
  brew install python
  ```
* **Create virtual environments**:

  ```bash
  python3 -m venv myenv
  source myenv/bin/activate
  ```

---

## 🧭 Ukubona Philosophy:

> "Every world-changing tool starts in an empty folder. You own the soil. Now grow something.”
 
