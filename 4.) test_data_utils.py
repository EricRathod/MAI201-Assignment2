
import re
import os
import pytest
import pandas as pd

# ── paste functions here so pytest can find them ──
def load_csv(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    df = pd.read_csv(filepath)
    if df.empty:
        raise ValueError("File is empty")
    return df

def clean_phone(phone):
    if phone is None:
        return ""
    digits = re.sub(r"\D", "", str(phone))
    if len(digits) == 11 and digits.startswith("1"):
        digits = digits[1:]
    return digits if len(digits) == 10 else ""

def validate_email(email):
    if not email or not isinstance(email, str):
        return False
    pattern = r"^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email.strip()))


# ── load_csv tests ────────────────────────────────
def test_load_csv_success(tmp_path):
    f = tmp_path / "test.csv"
    f.write_text("id,age\n1,25\n2,30\n")
    df = load_csv(str(f))
    assert len(df) == 2

def test_load_csv_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_csv("missing.csv")

def test_load_csv_empty_file(tmp_path):
    f = tmp_path / "empty.csv"
    f.write_text("id,age\n")
    with pytest.raises(ValueError):
        load_csv(str(f))


# ── clean_phone tests ─────────────────────────────
def test_clean_phone_dashes():
    assert clean_phone("719-808-4765") == "7198084765"

def test_clean_phone_dots():
    assert clean_phone("970.521.2218") == "9705212218"

def test_clean_phone_parentheses():
    assert clean_phone("(318) 414-9221") == "3184149221"

def test_clean_phone_plain():
    assert clean_phone("3637929158") == "3637929158"

def test_clean_phone_none():
    assert clean_phone(None) == ""

def test_clean_phone_invalid():
    assert clean_phone("-8437") == ""


# ── validate_email tests ──────────────────────────
def test_validate_email_valid():
    assert validate_email("user@example.com") is True

def test_validate_email_no_at():
    assert validate_email("userdomain.com") is False

def test_validate_email_starts_with_at():
    assert validate_email("@domain.com") is False

def test_validate_email_none():
    assert validate_email(None) is False

def test_validate_email_empty():
    assert validate_email("") is False
