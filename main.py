import sys
import os
import pyperclip
from src.database import DBHandler
from src.search import SearchEngine

# Library Rich untuk tampilan "Web" di Terminal
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.syntax import Syntax
from rich.prompt import Prompt
from rich import print as rprint

console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header(lang):
    console.print(Panel(
        f"[bold cyan]🚀 SNIPPET MANAGER[/bold cyan]\n[dim]Language: {lang.upper()}[/dim]",
        border_style="blue",
        title="[bold white]v1.0[/bold white]",
        title_align="right"
    ))

def main():
    language = "laravel-react"
    db = DBHandler(language)
    
    try:
        master_data = db.get_all_master_data()
        user_stats = db.get_stats()
        
        if not master_data:
            rprint(f"[bold red][!] Warning:[/bold red] Data tidak ditemukan di folder data/{language}")
            return

        clear_screen()
        while True:
            display_header(language)
            
            query = console.input("\n[bold yellow]🔍 Cari (Judul/Kategori/Tag):[/bold yellow] ").strip()
            
            if query.lower() == 'exit':
                rprint("\n[bold green]👋 Selamat ngoding, master![/bold green]")
                break
            
            if not query:
                clear_screen()
                continue

            results = SearchEngine.search(query, master_data, user_stats)

            if not results:
                rprint(f"\n[red]❌ Tidak ada hasil untuk: '{query}'[/red]")
                continue

            # --- TAMPILAN TABEL SEPERTI WEB ---
            table = Table(show_header=True, header_style="bold magenta", padding=(0, 1))
            table.add_column("No", justify="center", style="dim")
            table.add_column("Category", style="cyan")
            table.add_column("Title", style="white")
            table.add_column("Hits", justify="right", style="green")

            for idx, item in enumerate(results):
                fav = "⭐ " if item.get('is_favorite') else ""
                cat = item.get('category', 'general')
                table.add_row(str(idx + 1), cat, f"{fav}{item['title']}", str(item.get('hits', 0)))
            
            console.print(table)
            
            # 4. Interaksi
            choice = console.input("\n[bold blue]👉 Pilih nomor untuk LIHAT DETAIL[/bold blue] (Enter untuk cari lagi): ")
            
            if choice.isdigit() and 0 < int(choice) <= len(results):
                selected = results[int(choice) - 1]
                
                clear_screen()
                display_header(language)
                
                # --- TAMPILAN DETAIL DENGAN PANEL & SYNTAX HIGHLIGHTING ---
                # Menggunakan Syntax Highlighting (deteksi bahasa otomatis atau set ke php/javascript)
                code_snippet = Syntax(selected['code'], "php", theme="monokai", line_numbers=True)
                
                detail_info = f"[bold white]TITLE       :[/bold white] {selected['title']}\n"
                detail_info += f"[bold white]CATEGORY    :[/bold white] {selected.get('category', 'N/A')}\n"
                if selected.get('link'):
                    detail_info += f"[bold white]DOCS LINK   :[/bold white] [blue underline]{selected['link']}[/blue underline]\n"
                detail_info += f"[bold white]DESCRIPTION :[/bold white] [dim]{selected.get('description', '-')}[/dim]"

                console.print(Panel(detail_info, title="[bold green]Snippet Info[/bold green]", border_style="white"))
                console.print(Panel(code_snippet, title="[bold yellow]Source Code[/bold yellow]", border_style="yellow"))
                
                # 5. Konfirmasi Copy
                action = console.input("\n[bold cyan]Ketik 'c' untuk COPY, atau [Enter] untuk kembali:[/bold cyan] ").lower().strip()
                
                if action == 'c':
                    try:
                        pyperclip.copy(selected['code'])
                        rprint("[bold green]✅ KODE BERHASIL DI-COPY KE CLIPBOARD![/bold green]")
                    except Exception as e:
                        rprint(f"[bold red]❌ Gagal copy: {e}[/bold red]")

                # Update Stats
                s_id = selected['id']
                if s_id not in user_stats:
                    user_stats[s_id] = {"hits": 0, "is_favorite": False, "custom_tags": []}
                user_stats[s_id]['hits'] += 1
                db.save_stats(user_stats)
                
                console.input("\n[dim]Tekan [Enter] untuk kembali ke pencarian...[/dim]")
                clear_screen()
            else:
                clear_screen()

    except KeyboardInterrupt:
        rprint("\n\n[bold red][!] Program ditutup.[/bold red]")
        sys.exit(0)
    except Exception as e:
        console.print_exception(show_locals=True) # Menampilkan error ala "Web Debugger"

if __name__ == "__main__":
    main()