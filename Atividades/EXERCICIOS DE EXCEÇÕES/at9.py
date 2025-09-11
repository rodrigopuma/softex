"""Crie uma função sacar(saldo, valor) que:
Lance (raise) uma exceção personalizada SaldoInsuficienteError se o valor for maior que o saldo.
Caso contrário, retorne o novo saldo. Teste a função dentro de um try-except e exiba uma mensagem apropriada ao usuário."""

class SaldoInsuficienteError(Exception): ...

def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError(f"O valor que deseja sacar é maior que o seu saldo. Seu saldo é de R${saldo:.2f}.\nTente sacar um valor menor.")
    else:
        saldo -= valor
    return saldo
    
saldo = 3000
    
try: 
    saldo = sacar(saldo, 2000)
except SaldoInsuficienteError as erro:
    print(f"{type(erro).__name__}: {erro}")
else:
    print(f"Saldo: {saldo}")