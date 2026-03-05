from rich import print
from rich.table import Table #Tabela

#Criando tabeelas
tabela = Table(title="[yellow]Tabela de Preços[/]")

tabela.add_column("[blue]Nome[/]", justify="center")
tabela.add_column("[blue]Preço[/]", justify="center")
tabela.add_row("Mouse", '[green]R$300,00[/]', style="red")
tabela.add_row("Borracha", "[green]R$1,50[/]", style="red")

print(tabela)