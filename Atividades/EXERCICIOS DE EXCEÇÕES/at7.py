"""Peça ao usuário dois números e divida o primeiro pelo segundo. Trate dois tipos de erro:
ValueError se o usuário digitar algo inválido
ZeroDivisionError se tentar dividir por zero"""

try:
    numero = float(input("Digite um número: "))
    numero2 = float(input("Digite outro número: "))
    divisao = numero / numero2
except ValueError:
    print("Você precisa digitar apenas um número inteiro")
except ZeroDivisionError:
    print("O 2º número não pode ser 0.")
    