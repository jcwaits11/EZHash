# 🔐 EZHash — Secure File Hasher GUI (DevSecOps Project)

EZHash is a secure, Python-based desktop GUI application that computes cryptographic hashes (MD5, SHA-256, SHA-512) for user-selected files. Built with security-first principles and a full CI/CD pipeline, this project demonstrates DevSecOps practices across local development and GitHub integration.

---

## 🛠 Features

- 🖼 Simple GUI with Tkinter
- 📁 File selection (max ~5MB, safe types only)
- 🔐 Computes MD5, SHA-256, and SHA-512 hashes
- 🧼 Input validation + blocked dangerous file types
- 🕓 UTC timestamped hash log (locally saved)
- 💻 Local-only: no file uploads or internet dependency

---

## 🚧 DevSecOps CI/CD Workflow

This project uses **GitHub Actions** to automate secure code delivery.

### ✅ Tools Integrated

| Stage        | Tool         | Purpose                                |
|--------------|--------------|----------------------------------------|
| Linting      | `flake8`     | PEP8 style enforcement                 |
| Formatting   | `black`      | Consistent code formatting             |
| SAST         | `bandit`     | Detect insecure code patterns          |
| Dependency   | `pip-audit`  | Check for known vulnerable packages    |
| Secrets Scan | `gitleaks`   | Detect secrets in code                 |
| Testing      | `pytest`
