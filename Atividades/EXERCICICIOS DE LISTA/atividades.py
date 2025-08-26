# Primeira atividade

livros = ['Harry Potter', 'Senhor dos Aneis', 'Percy Jackson']
print(livros)

# Segunda atividade

print(livros[0], livros[-1])

# Terceira atividade

livros.append('Diario de um Banana')
livros.append('Jogos Vorazes')

# Quarta atividade

livros.insert(1, 'Duna')

# Quinta atividade

try:
    livros.remove('Silêncio dos inocentes')
except ValueError:
    print('Livro não foi encontrado')

# Sexta atividade

numeros = [1,2,3,2,4,2,5]
print(numeros.count(2))

# Setima atividade

for l in livros:
    print(f'O livro <{l}> é interessante')

# Oitava atividade

idades = [12, 18, 25, 14, 30]
for i in idades:
    if i >= 18:
        print(i)

# Nona atividade

valores = [10, 20, 30, 40]
soma = 0
for v in valores:
    soma += v

# Decima atividade

notas = []
for _ in range(2):
    notas_aluno = []
    for _ in range(3):
        nota = float(input('Digite uma nota: '))
        notas_aluno.append(nota)
    notas.append(notas_aluno)

for n in notas:
    soma = 0
    media = 0
    for nota_individual in n:
        soma += nota_individual
    media = soma / 3
    print(f'A média é {media}')

