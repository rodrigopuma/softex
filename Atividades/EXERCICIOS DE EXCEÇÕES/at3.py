"""Crie um programa que peça ao usuário um número inteiro. 
Se a conversão for bem-sucedida, mostre uma mensagem usando o bloco else."""

while True:
    try:
        numero = int(input("Digite um número inteiro: "))
    except ValueError:
        print("Você precisa digitar apenas um número inteiro")
        numero = int(input("Digite um número inteiro: "))
    else:
        print("Ok, seu número foi ", numero)
        break