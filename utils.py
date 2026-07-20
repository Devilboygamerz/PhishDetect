import os
import re
from datetime import datetime


REPORTS_DIR = "reports"


def create_reports_folder():
    """Create reports folder if it doesn't exist."""
    os.makedirs(REPORTS_DIR, exist_ok=True)


def is_valid_url(url):
    """Check whether a URL is valid."""
    pattern = re.compile(
        r"^(https?://)"
        r"([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}"
        r"(:\d+)?"
        r"(/.*)?$"
    )
    return bool(pattern.match(url))


def generate_report_name(url):
    """Generate a unique report filename."""
    domain = url.replace("https://", "").replace("http://", "")
    domain = domain.replace("/", "_")

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    return os.path.join(
        REPORTS_DIR,
        f"{domain}_{timestamp}.txt"
    )


def save_report(filename, content):
    """Save scan report."""
    create_reports_folder()

    with open(filename, "w", encoding="utf-8") as report:
        report.write(content)
