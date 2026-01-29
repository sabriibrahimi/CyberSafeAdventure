# Deploying CyberSafe Adventure to the Web

You have successfully built the web version of the game using `pygbag`.

## Local Testing
To test the game on your computer before uploading:
1. Open a terminal in this folder.
2. Run: `py -m pygbag .`
3. Open your browser to `http://localhost:8000`.

## Deployment to GitHub Pages (Manual Method)
1. Go to the `build/web` folder in your project.
2. This folder contains an `index.html` and other assets.
3. Upload **only the contents of this `build/web` folder** to a new GitHub repository (or a `gh-pages` branch of your current repo).
4. Go to the GitHub Repository Settings -> Pages.
5. Set the source to the branch you uploaded to (e.g., `main` or `gh-pages`) and the folder to `/` (root).
6. Your game will be live at `https://your-username.github.io/your-repo-name/`.

## Deployment to Itch.io
1. Go to the `build/web` folder.
2. Select all files inside it and zip them (Create a `.zip` file).
3. Create a new project on itch.io.
4. Set "Kind of project" to **HTML**.
5. Upload your `.zip` file.
6. Enable "This file will be played in the browser".
