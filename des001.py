from rich import print
from rich import inspect

class Funcionario:
    #Atributos de classe
    empresa = "Curso em Vídeo"
    def __init__(self, nome, setor, cargo):
        # atributos de instãncia
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self)->str:
        return f':handshake: Olá, sou [blue]{self.nome}[/] e sou [green]{self.cargo}[/] do setor de [red]{self.setor}[/] da empresa {Funcionario.empresa}'

c1 = Funcionario("Amanda", "Justiça", "Advogada")
print(c1.apresentacao())
#inspect(c1, methods=True, dunder=True)

c2 = Funcionario("Gaspar", "Programador",   "TI")
print(c2.apresentacao())

inspect(Funcionario)
inspect(c1)