# 1. Dobro dos números (map + lambda)
# Dada a lista [1, 2, 3, 4, 5], use map com lambda para gerar uma nova lista com o dobro de cada número.

lista = [1, 2, 3, 4, 5]
dobro = list(map(lambda n: n * 2, lista))

# 2. Filtrar pares (filter + lambda)
# Dada a lista [10, 15, 20, 25, 30], use filter com lambda para obter apenas os números pares.

lista = [10, 15, 20, 25, 30]
pares = list(filter(lambda n: n % 2 == 0, lista))

# 3. Soma dos números (reduce + lambda)
# Usando reduce, some todos os números da lista [1, 2, 3, 4, 5].

from functools import reduce

lista = [1, 2, 3, 4, 5]
soma = reduce(lambda x, y: x + y, lista)

# 4. Ordenação por comprimento da palavra (sorted + lambda)
# Dada a lista ["uva", "banana", "maçã", "laranja"], ordene as palavras pelo tamanho usando sorted e lambda.

lista = ["uva", "banana", "maçã", "laranja"]
lista_maior_para_menor = list(sorted(lista, key=lambda palavra: len(palavra), reverse=True)) # reverse true para ordenar do maior para o menor

# 5. Primeira letra maiúscula (map + lambda)
# Dada a lista ["ana", "pedro", "maria"], use map e lambda para transformar em ["Ana", "Pedro", "Maria"].

lista = ["ana", "pedro", "maria"]
pri_maiuscula = list(map(lambda nome: nome.capitalize(), lista))

# 6. Produto dos números (reduce + lambda)
# Usando reduce, calcule o produto (multiplicação) de todos os elementos da lista [2, 3, 4, 5].

from functools import reduce # importando de novo só pra relembrar que tem que importar

lista = [2, 3, 4, 5]
produto = reduce(lambda x, y: x * y, lista)

# 7. Ordenar por último caractere (sorted + lambda)
# Dada a lista ["banana", "uva", "maçã", "laranja"], ordene as palavras pelo último caractere.

lista = ["banana", "uva", "maçã", "laranja"]
ordena_ult_caractere = list(sorted(lista, key=lambda palavra: palavra[-1])) # ordenado em ordem alfabetica pelo ultimo caractere da pakavra
