import json
from pathlib import Path

REPORT = Path("/app/report.json")


def test_report_is_valid_json():
    """Criterion 2: Write a valid JSON file to /app/report.json."""
    assert REPORT.exists(), "report.json not found"
    data = json.loads(REPORT.read_text())
    assert isinstance(data, dict), "report.json is not a JSON object"


def test_total_requests():
    """Criterion 3 (total_requests) + Criterion 1: total_requests equals 6,
    confirming every line of access.log was read and parsed."""
    data = json.loads(REPORT.read_text())
    assert data.get("total_requests") == 6, (
        f"expected total_requests=6, got {data.get('total_requests')}"
    )


def test_unique_ips():
    """Criterion 3 (unique_ips): unique_ips equals 3."""
    data = json.loads(REPORT.read_text())
    assert data.get("unique_ips") == 3, (
        f"expected unique_ips=3, got {data.get('unique_ips')}"
    )


def test_top_path():
    """Criterion 3 (top_path): top_path is /index.html."""
    data = json.loads(REPORT.read_text())
    assert data.get("top_path") == "/index.html", (
        f"expected top_path='/index.html', got {data.get('top_path')}"
    )
