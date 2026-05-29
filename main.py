import sys
import os

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    ruta = sys.argv[1]

    if not os.path.exists(ruta):
        print(f"Error: File '{ruta}' not found.")
        sys.exit(1)

    if not ruta.endswith(".txt"):
        print("Error: Only .txt files are supported.")
        sys.exit(1)

    from stats import get_num_words, contar_veces, get_book_text, sorted_list, top_words
    from rich.console import Console
    from rich.table import Table
    from rich import print as rprint
    from rich.panel import Panel

    console = Console()
    libro = get_book_text(ruta)

    console.print(Panel(f"[bold cyan]📚 BookBot Report[/bold cyan]\n[dim]{ruta}[/dim]", expand=False))

    # Palabras totales
    total_palabras = get_num_words(libro)
    rprint(f"\n[bold green]Total words:[/bold green] {total_palabras:,}")

    # Top 10 palabras
    top = top_words(libro)
    table1 = Table(title="🔝 Top 10 Most Used Words", style="cyan")
    table1.add_column("Word", style="bold white")
    table1.add_column("Count", justify="right", style="green")
    for word, count in top:
        table1.add_row(word, f"{count:,}")
    console.print(table1)

    # Frecuencia de letras
    conteo_chars = contar_veces(libro)
    lista_sort = sorted_list(conteo_chars)

    table2 = Table(title="🔤 Character Frequency", style="magenta")
    table2.add_column("Character", style="bold white")
    table2.add_column("Count", justify="right", style="yellow")
    for l in lista_sort:
        if l["char"].isalpha():
            table2.add_row(l["char"], f"{l['num']:,}")
    console.print(table2)

main()