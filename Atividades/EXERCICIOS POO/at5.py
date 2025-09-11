"""Crie uma classe ContaBancaria com os atributos titular e saldo. Adicione um método depositar(valor) que aumenta o saldo e um método sacar(valor) 
que diminui o saldo (se houver saldo suficiente). Teste com depósitos e saques."""

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

conta = ContaBancaria("João", 1000)

conta.depositar(500)
conta.sacar(200)
print(conta.saldo)
