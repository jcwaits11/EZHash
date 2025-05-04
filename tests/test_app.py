# nosec B101
from pathlib import Path
from app import is_valid_file, compute_all_hashes


def test_valid_file_extension():
    assert is_valid_file(Path("document.txt")) is True
    assert is_valid_file(Path("report.pdf")) is True


def test_invalid_file_extension():
    assert is_valid_file(Path("malware.exe")) is False
    assert is_valid_file(Path("script.bat")) is False


def test_hashes_return_all_algorithms(tmp_path):
    # Create a dummy file
    test_file = tmp_path / "sample.txt"
    test_file.write_text("Hello, world!")

    hashes = compute_all_hashes(test_file)
    assert "MD5" in hashes
    assert "SHA-256" in hashes
    assert "SHA-512" in hashes
    assert len(hashes["SHA-256"]) == 64
