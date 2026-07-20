from rich.console import Console
from rich.table import Table

console = Console()

from banner import show_banner
from config import get_api_key
from scanner import submit_url, get_report

show_banner()

api_key = get_api_key()

url = input("\nEnter URL: ")

print("\nSubmitting URL...")

submit_url(url, api_key)

print("Waiting for analysis...\n")

import time
time.sleep(5)

report = get_report(url, api_key)

attributes = report["data"]["attributes"]

stats = attributes["last_analysis_stats"]

summary = Table(title="Scan Summary")

summary.add_column("Category", style="cyan")
summary.add_column("Count", justify="right")

summary.add_row("🔴 Malicious", str(stats["malicious"]))
summary.add_row("🟡 Suspicious", str(stats["suspicious"]))
summary.add_row("🟢 Harmless", str(stats["harmless"]))
summary.add_row("⚪ Undetected", str(stats["undetected"]))
summary.add_row("⏱ Timeout", str(stats["timeout"]))

console.print(summary)

vendors = attributes["last_analysis_results"]

vendor_table = Table(title="Security Vendors")

vendor_table.add_column("Vendor", style="cyan")
vendor_table.add_column("Verdict")

for vendor, result in vendors.items():
    verdict = result["category"]

    if verdict == "harmless":
        verdict = "[green]🟢 Harmless[/green]"

    elif verdict == "malicious":
        verdict = "[red]🔴 Malicious[/red]"

    elif verdict == "phishing":
        verdict = "[red]🎣 Phishing[/red]"

    elif verdict == "suspicious":
        verdict = "[yellow]🟡 Suspicious[/yellow]"

    elif verdict == "undetected":
        verdict = "[white]⚪ No Verdict[/white]"

    vendor_table.add_row(vendor, verdict)

console.print(vendor_table)
