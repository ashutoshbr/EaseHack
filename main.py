from rich.console import Console
from rich.table import Table

table = Table(expand=True, style="green", highlight=True)

table.add_column("Welcome to EaseHack", justify="center", no_wrap=True)
# table.add_column("Title", style="magenta")

table.add_row("👉 Press 1 to generate private & public key.")
table.add_row("👉 Press 2 to save a pair of key in .env.")
table.add_row("👉 Press 0 to exit.")

console = Console()
console.print(table)
