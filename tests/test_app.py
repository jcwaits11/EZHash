from pathlib import Path
from app import is_valid_file, compute_all_hashes


def test_valid_file_extension():
    assert is_valid_file(Path("document.txt")) is True  # nosec
    assert is_valid_file(Path("report.pdf")) is True  # nosec


def test_invalid_file_extension():
    assert is_valid_file(Path("malware.exe")) is False  # nosec
    assert is_valid_file(Path("script.bat")) is False  # nosec


def test_hash_computation():
    test_file = Path("tests/sample.txt")
    test_file.write_text("Test content")

    hashes = compute_all_hashes(test_file)
    assert "MD5" in hashes  # nosec
    assert "SHA-256" in hashes  # nosec
    assert "SHA-512" in hashes  # nosec
    assert len(hashes["SHA-256"]) == 64  # nosec

    test_file.unlink()
