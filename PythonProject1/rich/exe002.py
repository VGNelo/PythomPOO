from rich.panel import Panel  #importando da biblioteca panel, Panel (P maiúsculo)
from rich import print  #importando biblioteca print

caixa = Panel('[white]Esse aqui é um painel de exemplo.[/] :+1:', title="CAIXA/MENSAGEM", style= "red", width=40)
print(caixa)