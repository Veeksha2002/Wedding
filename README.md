# Wedding invitation - Local server

This repository contains a single static HTML invitation `Wed.html` and a tiny Flask app to serve it locally.

Quick start (Windows PowerShell):

```powershell
# Create and activate a virtual environment (optional but recommended)
python -m venv .venv; .\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

# Then open http://127.0.0.1:5000/ in your browser
```

Notes:
- Put your `Wed.jpg` image into the project's `static/` folder so it is served by Flask. Example (PowerShell):

```powershell
Copy-Item 'C:\Users\User\Documents\Wedding\Wed.jpg' -Destination .\static\Wed.jpg
```

- The template uses `{{ url_for('static', filename='Wed.jpg') }}` so the image will load when the server is running.
- The server includes a `/health` endpoint for quick checks.
