# Cryptography library used for MD5, SHA-256, and SHA-512 hashing
import hashlib
import tkinter as tk  # GUI library for building a desktop app
from tkinter import filedialog, messagebox
from datetime import datetime  # For UTC timestamping of hash logs
from pathlib import Path  # Secure and clean file path handling

# File Extension Whitelisting and Blacklisting
# Blocked file types
BLOCKED_EXTENSIONS = {
    ".exe",
    ".bat",
    ".cmd",
    ".sh",
    ".vbs",
    ".js",
    ".msi",
    ".dll",
    ".scr",
}

# Allowed file types
ALLOWED_EXTENSIONS = {
    ".txt",
    ".pdf",
    ".jpg",
    ".jpeg",
    ".png",
    ".csv",
    ".xlsx",
    ".xls",
    ".docx",
    ".doc",
    ".mp3",
    ".mp4",
    ".zip",
    ".rar",
    ".json",
    ".xml",
    ".log",
}


# Validate if file extension is allowed and safe
def is_valid_file(path):
    suffix = path.suffix.lower()
    return suffix in ALLOWED_EXTENSIONS and suffix not in BLOCKED_EXTENSIONS


# Compute MD5, SHA-256, and SHA-512 hashes for a file
def compute_all_hashes(file_path):
    try:
        with open(file_path, "rb") as f:
            content = f.read()
        return {
            "MD5": hashlib.md5(content).hexdigest(),
            "SHA-256": hashlib.sha256(content).hexdigest(),
            "SHA-512": hashlib.sha512(content).hexdigest(),
        }
    except Exception as e:
        return {"Error": str(e)}


# Log hash results to a local file with timestamp
def log_hashes(filename, hashes):
    timestamp = datetime.utcnow().isoformat()
    with open("hash_log.txt", "a") as log:
        for algo, value in hashes.items():
            log.write(f"{timestamp} - {filename} - {algo} - {value}\n")


# Launch GUI Application
def launch_gui():
    # GUI button: browse and select a file
    def choose_file():
        path = filedialog.askopenfilename()
        if path:
            file_path_var.set(path)

    # GUI button: validate, compute, display, and log hashes
    def run_hash():
        path = Path(file_path_var.get())
        if not path.exists():
            messagebox.showerror("Error", "Selected file does not exist.")
            return
        if not is_valid_file(path):
            messagebox.showerror("Error", f"File type '{path.suffix}' is not allowed.")
            return

        hashes = compute_all_hashes(path)
        if "Error" in hashes:
            messagebox.showerror("Error", hashes["Error"])
            return

        # Format the hash results and display them
        result_text = f"File: {path.name}\n"
        for algo, hash_val in hashes.items():
            result_text += f"{algo}: {hash_val}\n"

        result_var.set(result_text)
        log_hashes(path.name, hashes)

    # GUI Window and Layout
    root = tk.Tk()
    root.title("Secure File Hasher")

    file_path_var = tk.StringVar()
    result_var = tk.StringVar()

    # GUI Elements: label, input, button, result display
    tk.Label(root, text="Select File:").pack()
    tk.Entry(root, textvariable=file_path_var, width=50).pack()
    tk.Button(root, text="Browse", command=choose_file).pack()
    tk.Button(root, text="Compute Hashes", command=run_hash).pack(pady=10)

    tk.Label(root, textvariable=result_var, wraplength=500, justify="left").pack(pady=5)

    root.mainloop()


# === Run the GUI ===
launch_gui()
