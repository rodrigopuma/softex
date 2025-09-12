"""Na classe, ContaBancaria, converta saldo para uma atributo privado. 
Crie um método setter e um getter para acessar e modificar essa atributo, 
seguindo uma regra lógica (Ex: saldo não pode ser negativo)"""

import datetime

class ContaBancaria:
    # Atributos
    def __init__(self, titular, num_conta, saldo=0.0):
        self.titular = titular
        self.num_conta = num_conta
        self.__saldo = float(saldo)
        self.operacoes = []

    def __str__(self):
        return f"Conta n {self.num_conta} do titular {self.titular} tem {self.__saldo} de saldo"
    
    def __repr__(self):
        return f"ContaBancaria(titular={self.titular!r},num_conta={self.num_conta!r}, saldo={self.__saldo!r})"
    
    # Metodo
    def deposito(self, valor):
        self.__saldo += valor
        data_operacao = datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
        self.operacoes.append([data_operacao, "Deposito", valor])
        print(f"Foi depositado {valor} reais na sua conta")
    
    def saque(self, valor):
        if self.__saldo < valor:
            print("Saldo insuficiente para o valor do saque.")
        else:
            self.__saldo -= valor
        self.__saldo -= valor
        data_operacao = datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
        self.operacoes.append([data_operacao, "Saque", valor])
        print(f"Foi sacado {valor} reais na sua conta")

    def extrato(self):
        for operacao in self.operacoes:
            print(operacao)
        print(f"Saldo: {self.__saldo}")
    

    # Setter
    def set_saldo(self, valor):
        if self.__saldo < valor:
            print("Saldo insuficiente, o saldo não pode ficar negativo")
        else:
            self.__saldo = valor
            print("Saldo atualizado com sucesso")
    
    # Getter
    def get_saldo(self):
        return float(self.__saldo)


