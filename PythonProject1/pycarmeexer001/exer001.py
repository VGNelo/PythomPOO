class Gafanhoto:
    def __init__(self):
        self.nome = ''
        self.idade = 0

    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é um Gafanhot e tem {self.idade} anos"


# Testando
g = Gafanhoto()
g.nome = "Valdemir"
g.idade = 30

print(g.mensagem())   # Valdemir tem 30 anos
g.aniversario()
print(g.mensagem())   # Valdemir tem 31 anos

g1 = Gafanhoto()
g1.nome = "Amanda"
g1.idade = 48

print(g1.mensagem())
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Manuelle"
g2.idade = 13


print(g2.mensagem())
g2.aniversario()
print(g2.mensagem())