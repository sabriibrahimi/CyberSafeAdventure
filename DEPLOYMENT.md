# 🚀 How to Deploy Your Game to the Web

You can easily host this game on **GitHub Pages** so anyone can play it via a link! We use a tool called `pygbag` to convert your Python game to a Web version.

## Step 1: Install Pygbag
Open your terminal and run:
```bash
pip install pygbag
```

## Step 2: Build the Web Version
Run this command in your project folder (where `main.py` is):
```bash
python -m pygbag --build main.py
```
*   This will create a new folder called `build`.
*   Inside `build`, there is a `web` folder. This is your game website!

## Step 3: Prepare for GitHub Pages
GitHub Pages loves simple setups. The easiest way is to use a `/docs` folder.

1.  **Rename** the `build/web` folder to `docs`.
    *   Take the `web` folder *out* of `build` if you want, or just rename `build/web` to `docs` and move it to the root of your project.
    *   **Structure:** Your project folder should look like:
        ```
        Project/
          main.py
          src/
          docs/  <-- This was the "web" folder
            index.html
            ...
        ```

2.  **Test it (Optional):**
    *   If you want to run it locally before uploading, you can run: `python -m pygbag main.py` and open `localhost:8000`.

## Step 4: Upload to GitHub
1.  Commit your changes, including the new `docs` folder.
    ```bash
    git add .
    git commit -m "Build web version"
    git push
    ```

## Step 5: Activate GitHub Pages
1.  Go to your **GitHub Repository** page.
2.  Click on **Settings** (Top right tab).
3.  On the left sidebar, click **Pages**.
4.  Under **Build and deployment > Source**, select **Deploy from a branch**.
5.  Under **Branch**, select `main` (or `master`) and change the folder from `/(root)` to `/docs`.
6.  Click **Save**.

## 🎉 Done!
Wait about 1-2 minutes. Refresh the Settings page. GitHub will show you a link (e.g., `https://username.github.io/repo-name/`).
Share that link with your friends!
