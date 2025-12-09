# 1. Crie um dicionário simples
#        Crie um dicionário chamado aluno com as chaves: "nome", "idade" e "nota", e preencha com valores fictícios.
aluno = {
    "nome": "Artur",
    "idade": 15,
    "nota": 10.0
}


# 2. Acessando valores
#        Dado o dicionário:
produto = {"nome": "Caneta", "preço": 2.5, "estoque": 100}
#        Imprima o nome do produto e a quantidade em estoque.
print(f"\nNome do Produto: {produto["nome"]}\nQuantidade em estoque: {produto["estoque"]}\n")


# 3. Adicionando novos pares chave-valor
#        Dado o dicionário:
pessoa = {"nome": "Carlos", "idade": 30}
#        Adicione uma nova chave "cidade" com valor "São Paulo".
pessoa["cidade"] = "São Paulo"


# 4. Removendo elementos
#        Dado o dicionário:
carro = {"marca": "Ford", "modelo": "Fiesta", "ano": 2010}
#        Remova a chave "ano" do dicionário.
carro.pop("ano")



# 5. Verificando existência de uma chave
#        Verifique se a chave "telefone" existe no dicionário:
contato = {"nome": "Ana", "email": "ana@email.com"}
print(f"Contato tem telefone: {contato.__contains__("telefone")}")


# 6. Contando frequência de palavras
#        Escreva uma função que receba uma lista de palavras e retorne um dicionário com a contagem de cada palavra.
palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]

def contagem_palavra(palavras: list) -> dict:
    contagem = {}
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    return contagem

print(contagem_palavra(palavras))


# 7. Invertendo um dicionário
#        Dado o dicionário:
d = {"a": 1, "b": 2, "c": 3}
#        Crie um novo dicionário invertendo as chaves e os valores: {1: "a", 2: "b", 3: "c"}.
inv_d = {}
for key, value in d.items():
    inv_d[value] = key
print(inv_d)


# 8. Dicionário com listas
#        Crie um dicionário onde cada chave é o nome de um aluno e o valor é uma lista com 3 notas. Depois, imprima a média de cada aluno.
turma = {
    "Artur": [10.0, 8.8, 6.9],
    "João": [5.3, 9.7, 8.5],
    "Maria": [10.0, 9.6, 9.8]
}

for aluno, notas in turma.items():
    print(f"Média de {aluno}: {sum(notas) / len(notas) :.1f}")


# 9. Mesclando dois dicionários
#        Escreva uma função que recebe dois dicionários e retorna um novo dicionário contendo todos os pares chave-valor. Se houver chaves repetidas, o valor do segundo dicionário deve prevalecer.
def sobrescrever_dicionarios(dict1: dict, dict2: dict) -> dict:
    new_dict = {}
    for key, value in dict1.items():
        new_dict[key] = value
    for key, value in dict2.items():
        new_dict[key] = value
    return new_dict


# 10. Ordenando dicionário por valor
#        Dado o dicionário:
pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}
pontuacoes_ordenadas = dict(sorted(pontuacoes.items(), key=lambda x: x[1], reverse=True))
#        Imprima os itens do dicionário ordenados pela pontuação (valor), do maior para o menor.
print(pontuacoes_ordenadas)
