"""1) Crie uma função chamada saudacao que imprime na tela a mensagem "Olá, bem-vindo ao Python!". Em seguida, chame a função no programa."""

def saudacao():
    print('Olá, bem-vindo ao Python!')

saudacao()

"""2) Crie uma função chamada dobro que recebe um número como parâmetro e retorna o dobro desse número. 
Teste chamando a função com diferentes valores."""

def dobro(numero: float):
    return numero * 2

print(dobro(2))
print(dobro(4))

"""3) Crie uma função chamada soma que receba dois números e retorne a soma deles. Depois, use a função para somar 10 + 20."""

def soma(num1: float, num2: float):
    return num1 + num2

soma(10, 20)

"""4) Crie uma função chamada mensagem que receba um nome como parâmetro e exiba a mensagem: "Olá, [nome]!" 
Caso o nome não seja informado, mostre "Olá, visitante!"."""

def mensagem(nome=''):
    print('Olá, visitante!') if nome == '' else print(f'Olá, {nome}!')

"""5) Crie uma função chamada operacoes que receba dois números e retorne a soma, a subtração e a multiplicação deles."""

def operacoes(num1: float, num2: float, soma=False, subtracao=False, multiplicacao=False):
    """Faz operações de soma, subtração e multiplicação apenas uma por vez. Para usar apenas a operação desejada para True

    Args:
        num1 (float): Numero 1
        num2 (float): Numero 2
        soma (bool, optional): Operação de soma, alterar para True se desejado. Por padrão False.
        subtracao (bool, optional): Operação de subtração, alterar para True se desejado. Por padrão False.
        multiplicacao (bool, optional): Operação de multiplicação, alterar para True se desejado. Por padrão False.

    Returns:
        float: Retorna apenas o resultado da operação escolhida
    """
    if soma is False and subtracao is False and multiplicacao is False:
        print('Você precisa selecionar uma operação.')
    
    if ((soma is True) and (subtracao is True)) or ((soma is True) and (multiplicacao is True)) or ((subtracao is True) and (multiplicacao is True)):
        print("Não é possivel retornar duas ou mais operações ao mesmo tempo")
        if soma is True:
            print(f'Soma: {num1 + num2}')

        if subtracao is True:
            print(f'Subtração: {num1 - num2}')

        if multiplicacao is True:
            print(f'Multiplicação: {num1 * num2}')
        return 'coloque apenas uma operação como verdadeira'
    else:
        if soma is True:
            return num1 + num2
        
        if subtracao is True:
            return num1 - num2
        
        if multiplicacao is True:
            return num1 * num2
        
        
operacoes(10, 2, True, True, True) # Ele apenas vai printar as 3 operações, mas não retornara

mult = operacoes(4, 8, multiplicacao=True) # Ele irá apenas retornar o valor da multiplicação de 4 e 8

"""6) Crie uma função chamada media que receba uma quantidade variável de números e retorne a média deles. Teste com 3, 5 e 7 valores diferentes."""

def media(*args):
    soma = sum(args)
    media = soma / len(args)
    return media

print(media(3, 5, 9, 1, 4))
print(media(3, 5, 9, 1, 4, 6, 10))
print(media(5, 5, 8))

"""7) Crie uma função chamada dados_pessoais que receba informações de uma pessoa (nome, idade, cidade, etc.) usando **kwargs e imprima cada dado em uma linha. Exemplo de chamada:"""

def dados_pessoais(**kwargs):
    for dados, informacao in kwargs.items():
        print(f'{dados.capitalize()}: {informacao}')

dados_pessoais(nome='Rodrigo', idade=18, cidade='Recife')

"""8) Crie uma função chamada calculadora que tenha dentro dela outras funções (somar, subtrair, multiplicar, dividir). 
A função principal deve permitir escolher a operação e retornar o resultado."""

def somar(n1, n2):
    return n1 + n2
def subtrair(n1, n2):
    return n1 - n2
def multiplicar(n1, n2):
    return n1 * n2
def dividir(n1, n2):
    return n1 / n2

def calculadora(n1: float, n2: float):
    operacao = input('Escolha a operação desejada ["+", "-", "*", "/"]: ')
    while operacao not in ['+', '-', '*', '/']:
        operacao = input('Entrada inválida selecione alguma valida ["+", "-", "*", "/"]: ')
        
    if operacao == '+':
        calculo = somar(n1, n2)
    elif operacao == '-':
        calculo = subtrair(n1, n2)
    elif operacao == '*':
        calculo = multiplicar(n1, n2)
    elif operacao == '/':
        calculo = dividir(n1, n2)
    
    print(f'{n1} {operacao} {n2} = {calculo}')
    return calculo

calculadora(3, 5)

"""9) Crie uma função chamada aplicar_operacao que receba dois números e uma função como parâmetros. 
A função deve aplicar a operação recebida (ex: soma, multiplicação). Exemplo:"""

def soma(n1, n2):
    return n1 + n2
def subtracao(n1, n2):
    return n1 - n2
def multiplicao(n1, n2):
    return n1 * n2
def divisao(n1, n2):
    return n1 / n2

def aplicar_operacao(num1: float, num2: float, operacao):

    print(f'A {operacao.__name__} de {num1} e {num2} é {operacao(num1, num2)}')
    return operacao(num1, num2)

aplicar_operacao(3, 5, subtracao)
