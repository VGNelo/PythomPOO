from rich import print
from rich.panel import Panel
class produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} custa R${self.preco:,.2f} "

    def etiqueta(self):
        conteudo = f"{self.nome.center(30, ' ')}"
        conteudo += f"{'-' * 30}"
        precof = f"R${self.preco:,.2f}"
        conteudo += f"{precof.center(30, '*')}"
        etiqueta = Panel(conteudo, title="Produto", width=34)
        print(etiqueta)
p1 = produto("Iphone 17 Pro Max", 25_00.85)
p2 = produto("Notebook Gamer", 8_000)

p1.etiqueta()
p2.etiqueta()