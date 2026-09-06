# Flask CI/CD Microservice 🚀

A lightweight Python Flask microservice built specifically for hands-on **CI/CD (Continuous Integration & Continuous Deployment)** learning with **GitHub Actions**.

---

## 📂 Project Structure

```
.
├── app/
│   ├── __init__.py
│   └── main.py          # REST API endpoints (/, /health, /api/add)
├── tests/
│   ├── __init__.py
│   └── test_main.py     # Pytest unit tests
├── Dockerfile            # Container image specification (non-root)
├── requirements.txt      # Python dependencies (Flask, Pytest, Flake8)
├── .gitignore            # Files excluded from git
└── README.md             # This guide
```

---

## 🛠️ Local Testing & Execution

### 1. Install Dependencies
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Run the Unit Tests (CI Phase)
```bash
pytest tests/ -v
```

### 3. Check Code Formatting & Syntax (Linting)
```bash
flake8 app/ tests/ --max-line-length=120
```

### 4. Run the Application
```bash
python -m flask --app app.main:app run --port 5000
```
Test endpoints:
- Welcome: `curl http://localhost:5000/`
- Health: `curl http://localhost:5000/health`
- Add API: `curl -X POST http://localhost:5000/api/add -H "Content-Type: application/json" -d '{"a": 10, "b": 25}'`

### 5. Build and Test Docker Container
```bash
docker build -t flask-cicd-pipeline:latest .
docker run -p 5000:5000 flask-cicd-pipeline:latest
```

---

## 🎯 Next Step: Writing Your GitHub Actions CI/CD Pipeline

To set up CI/CD, you will create `.github/workflows/ci.yml` in this repository.

### What Your Pipeline Needs to Do:
1. **Trigger**: Run whenever code is pushed to `main` or on a Pull Request.
2. **Job 1 (CI - Continuous Integration)**:
   - Checkout repository (`actions/checkout@v4`).
   - Set up Python environment (`actions/setup-python@v5`).
   - Install dependencies (`pip install -r requirements.txt`).
   - Run linter (`flake8`).
   - Run tests (`pytest`).
3. **Job 2 (CD - Continuous Delivery)**:
   - Only run if Job 1 passes!
   - Build Docker container image.
   - Tag and push to GitHub Container Registry (`ghcr.io`) or Docker Hub.
