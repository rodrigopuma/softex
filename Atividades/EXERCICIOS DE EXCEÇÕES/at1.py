"""Escreva um programa que peça ao usuário para digitar um número. 
Trate o erro caso ele digite algo que não seja um número inteiro."""

while True:
    try:
        numero = int(input("Digite um número inteiro: "))
    except ValueError:
        print("Você precisa digitar apenas um número inteiro")
        numero = int(input("Digite um número inteiro: "))
    else:
        print("Ok, seu número foi ", numero)
        break