"""
Creates sample test_data.xlsx for data-driven login tests.
Columns: username | password | expected_result (SUCCESS | ERROR).
"""

from pathlib import Path

from openpyxl import Workbook

# Practicetestautomation.com valid credentials (documented on their page)
VALID_USER = "student"
VALID_PASS = "Password123"

OUTPUT_FILE = "test_data.xlsx"
HEADERS = ["username", "password", "expected_result"]
ROWS = [
    (VALID_USER, VALID_PASS, "SUCCESS"),
    ("wronguser", "wrongpass", "ERROR"),
    ("student", "wrongpass", "ERROR"),
    ("invalid", VALID_PASS, "ERROR"),
]


def main():
    path = Path(__file__).resolve().parent / OUTPUT_FILE
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    ws.append(HEADERS)
    for row in ROWS:
        ws.append(row)
    wb.save(path)
    print(f"Created {path} with {len(ROWS)} data rows.")


if __name__ == "__main__":
    main()
