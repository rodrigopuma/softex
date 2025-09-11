"""Crie uma função dividir(a, b) que lance (raise) uma exceção ZeroDivisionError se b for igual a zero. 
Caso contrário, retorne o resultado da divisão."""

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("O 2º parâmetro não pode ser 0, pois não é possivel dividir por 0.")
    else:
        print(f"A divisão é {a} / {b} = {a / b}")

dividir(1, 1)
dividir(1, 0)