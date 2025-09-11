"""Crie um programa que peça ao usuário um número inteiro e verifique se ele é par. Use:
try para a conversão,
else para verificar se é par ou ímpar,
finally para exibir "Fim do programa"."""

try:
    n = float(input("Digite um número inteiro: "))
except ValueError:
    print("Você precisa digitar apenas um número inteiro")
else:
    print(f"O número {n} é {'par' if n % 2 == 0 else 'ímpar'}")
finally:
    print("Fim do programa.")