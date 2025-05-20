Here’s a simple, 10-minute plan to get your high school intern up and running with VS Code on his Mac. Think of this as a clean, guided rite of passage—not into complexity, but into creative control.

---

### 🧭 1. **Download & Install VS Code** (2 min)

* Go to [https://code.visualstudio.com](https://code.visualstudio.com)
* Click “Download for Mac (Intel or Apple Silicon)” — whichever matches his system.
* Open the `.zip` and drag VS Code into the **Applications** folder.

---

### ⚙️ 2. **Open VS Code & Install Essentials** (3 min)

* Launch VS Code.
* When prompted, allow it access to the system files.
* Click the **Extensions** icon (left bar) and install:

  * ✅ **Python** (if you’ll be using Python)
  * ✅ **Prettier** (for clean formatting)
  * ✅ **GitHub Copilot** (if you want AI help, optional)

---

### 📂 3. **Open a Project Folder** (2 min)

* Create a new folder on the Desktop called `intern-project`.
* In VS Code: `File > Open Folder...` and select `intern-project`.

---

### 🧪 4. **Make and Run a Test File** (2 min)

* Inside VS Code, right-click in the folder → `New File` → name it `test.py`
* Type:

  ```python
  print("Hello, Ukubona!")
  ```
* Hit `Run` ▶️ (it may prompt to install the Python extension or interpreter—let it).

---

### 🌱 5. **Tell Him This is the Seed** (1 min)

Let him know:

* Every great app, dashboard, or tool starts in a folder like this.
* He now owns the soil—the code is just what grows in it.

---

Perfect—this is his first real *push* into the world. To get `index.html` from his Mac into a GitHub repo, we just need a few clear steps. Here's how to do it, boiled down to one decisive question and a simple 5-step follow-up.

---

### ❓ The Question to Ask Him:

**"Do you already have a GitHub account? If not, let's make one real quick."**

(If he doesn't, spend 2 minutes to create one at [github.com](https://github.com), with email verification.)

---

### 🚀 Push Workflow (Assuming `index.html` is ready in a folder)

#### 1. **Install Git (if not already installed)**

* Open **Terminal**
* Type: `git --version`
* If it's not installed, it will prompt him to install Xcode Command Line Tools. Click **Install**.

#### 2. **Set Up Git (first time only)**

```bash
git config --global user.name "Jonathan Gasaatura"
git config --global user.email "jonathan@example.com"
```

#### 3. **Create a New Repo on GitHub**

* Go to GitHub → `+` → **New repository**
* Name it (e.g. `intern-project`)
* Keep it **public**, **no README**, and click **Create repository**

#### 4. **In Terminal: Initialize and Push**

```bash
cd ~/Desktop/intern-project  # or wherever his folder is
git init
git add index.html
git commit -m "first commit"
git remote add origin https://github.com/USERNAME/intern-project.git
git branch -M main
git push -u origin main
```

(Substitute `USERNAME` with his GitHub username.)

#### 5. **Celebrate**

* Go to the repo in his browser → refresh → 🎉 his `index.html` is live.

---

Let me know if you want this to deploy to GitHub Pages next. That’s a beautiful follow-up to say: *your code lives on the internet now.*
