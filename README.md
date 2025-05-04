# EZHash

A secure, local-only Python GUI app that hashes files using MD5, SHA-256, and SHA-512. Designed with a full DevSecOps CI/CD pipeline.

---

## 🔐 Features

- Choose any allowed file from your system
- Computes all three hashes (MD5, SHA-256, SHA-512)
- GUI built with `tkinter` (no web browser needed)
- Input validation blocks dangerous file types (e.g., `.exe`, `.bat`)
- Logs hash results with UTC timestamp to `hash_log.txt`
- No files are uploaded or stored — runs 100% locally

---

## 🛠️ DevSecOps Tools (CI/CD)

Automated GitHub Actions pipeline includes:

- ✅ `black` – code formatting
- ✅ `flake8` – Python linting
- ✅ `bandit` – static code security analysis
- ✅ `pip-audit` – Python dependency vulnerability scanning
- ✅ `gitleaks` – secrets scanning
- ✅ `pytest` – basic unit tests

---

## 🚀 How to Run

1. Clone the repo:

   ```bash
   git clone https://github.com/jcwaits11/EZHash.git
   cd EZHash
