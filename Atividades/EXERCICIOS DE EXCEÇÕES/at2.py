"""Peça ao usuário dois números e tente multiplicá-los. 
Se o usuário digitar algo inválido, exiba uma mensagem de erro."""

try:
    numero = float(input("Digite um número: "))
    numero2 = float(input("Digite outro número: "))
except ValueError:
    print("Você precisa digitar apenas um número inteiro")
else:
    print(f"A multiplicação é {numero} x {numero2} = {numero * numero2}")