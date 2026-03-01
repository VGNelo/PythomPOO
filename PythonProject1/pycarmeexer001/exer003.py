class ContaBancaria:
    '''
    Cria uma conta bancaria e permite fazer saques e depositos
    '''

    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.titular = nome
        self.saldo = saldo

    def mensagem_criacao(self):
        return f"Conta {self.id} criada com sucesso, saldo atual R${self.saldo:.2f}"

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:.2f}"

    def depositar(self, valor):
        self.saldo += valor
        return f'Deposito de R${valor:.2f} autorizado na conta {self.id}'

    def sacar(self, valor):
        if valor > self.saldo:
            return f'Valor de saque NEGADO de R${valor:.2f} na conta de {self.id}, SALDO INSUFICIENTE'
        else:
            self.saldo -= valor
            return f'Saque de R${valor:.2f} autorizado na conta de {self.id}'


# Testando
c1 = ContaBancaria(112, "Gaspar", 3000)

print(c1.mensagem_criacao())   # mostra mensagem de criação
print(c1.depositar(500))       # mostra mensagem de depósito
print(c1.sacar(30000))         # mostra mensagem de saque negado
print(c1.sacar(2000))          # mostra saque autorizado
print(c1)                      # mostra saldo final