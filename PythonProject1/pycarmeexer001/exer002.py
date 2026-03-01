class Gafanhoto:
    '''
    Essa classe cria um gafanhoto que tem nome e idade
    Paraa criar uma nova pessoa use:
    variavel = Gafanhoto(nome e idade)
    '''
    def __init__(self, nome = "", idade = 0):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1

    def __str__(self):  #Dunder Method
        return f"{self.nome} é um Gafanhot e tem {self.idade} anos"


# Testando
g = Gafanhoto("Valdemir", 30)
print(g)  # Valdemir tem 30 anos
g.aniversario()
print(g)   # Valdemir tem 31 anos

g1 = Gafanhoto("Amanda", 48)

print(g1)
g1.aniversario()
print(g1)

print(g1.__doc__)