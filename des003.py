from rich import print
from rich.panel import Panel

class churrasco:
    #atributo de class
    consumo_padrao:float = 0.400 #cada pessoa come em média 400g de carrne
    preco_kg:float = 82.40 #cada kg de carne custa R$ 82.40

    def __init__(self, titulo, quant):
        #Atributos de instancia
        self.titulo = titulo
        self.participantes = quant

    def __str__(self):
        return f"Esse é o {self.titulo} com {self.participantes} pessoas participando"

    def calcular_qtd_carne(self) -> float:
        return self.participantes * churrasco.consumo_padrao
    def calcular_custo_total(self) -> float:
        return self.calcular_qtd_carne() * self.__class__.preco_kg # pode ser assim churrasco.preco_kg

    def calcular_custo_individuaal(self) -> float:
        return self.calcular_custo_total() / self.participantes

    def analisar(self):
        conteudo = f"Analisando, [green]{self.titulo}[/] com [blue]{self.participantes}[/] convidados"
        conteudo += f"\nCada participante comera [red]{churrasco.consumo_padrao}[/] KG e cada KG custa [red]R${churrasco.preco_kg:.2f}[/]"
        conteudo += f"\nRecomendo comprar [blue]{self.calcular_qtd_carne():.3f}[/]KG de carne,"
        conteudo += f"\no custo total será de [green]R${self.calcular_custo_total():.2f}[/]"
        conteudo += f"\nCadda pessoa pagara [yellow]R${self.calcular_custo_individuaal():.2f}[/]"
        painel = Panel(conteudo, title = self.titulo)
        print(painel)

c1 = churrasco("Churrasco dos Amigos", 15)
c1.analisar()

c2 = churrasco("Festa do fim de ano", 80)
c2.analisar()