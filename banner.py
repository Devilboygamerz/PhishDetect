from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich import box

console = Console()

TOOL_NAME = "PhishDetect"
VERSION = "1.0.0"
AUTHOR = "Inshad Ameer"
GITHUB = "@Devillboygamerz"
INSTAGRAM = "@_ameer_734"


def show_banner():
    banner = r"""
██████╗ ██╗  ██╗██╗███████╗██╗  ██╗
██╔══██╗██║  ██║██║██╔════╝██║  ██║
██████╔╝███████║██║███████╗███████║
██╔═══╝ ██╔══██║██║╚════██║██╔══██║
██║     ██║  ██║██║███████║██║  ██║
╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝
"""

    body = Text()
    body.append(banner, style="bold yellow")
    body.append("\n")
    body.append("Professional Phishing Detection Tool\n", style="bold white")
    body.append("Powered by VirusTotal API\n\n", style="cyan")

    body.append("Author     : ", style="bold green")
    body.append(f"{AUTHOR}\n")

    body.append("GitHub     : ", style="bold green")
    body.append(f"{GITHUB}\n")

    body.append("Instagram  : ", style="bold green")
    body.append(f"{INSTAGRAM}\n")

    body.append("Version    : ", style="bold green")
    body.append(f"v{VERSION}")

    console.print(
        Panel(
            Align.center(body),
            title="[bold yellow]PhishDetect[/bold yellow]",
            subtitle="[green]Ready to Scan[/green]",
            border_style="yellow",
            box=box.ROUNDED,
            padding=(1, 3),
        )
    )
