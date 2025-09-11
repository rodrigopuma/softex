"""Modifique a classe ContaBancaria para que o método sacar retorne True se a operação for bem-sucedida e False caso contrário. Teste o retorno e imprima mensagens adequadas."""

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print("Operação realizada com sucesso")
            return True
        else:
            print("Saldo insuficiente")
            return False

conta = ContaBancaria("João", 1000)

conta.depositar(500)
print(conta.saldo)

print(conta.sacar(2000))
print(conta.saldo)

print(conta.sacar(500))
print(conta.saldo)