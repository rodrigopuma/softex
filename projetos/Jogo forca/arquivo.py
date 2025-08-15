import json
import random as rdm

ARQUIVO_PALAVRAS = './palavras.json'

def ler_palavras():
    """Lê a lista de categorias e palavras no json pega a categoria e palavra

    Returns:
        str: categoria
        str: palavra
        int: tamanho
    """
    with open(ARQUIVO_PALAVRAS, 'r', encoding='utf-8') as arquivo:
        lista_palavras = list(json.load(arquivo))
    indice = rdm.randint(0, (len(lista_palavras) - 1))
    categoria_palavra = lista_palavras[indice]
    for c in categoria_palavra.keys(): # for para pegar a categoria da palavra
        categoria = c
    lista_palavras_categoria = categoria_palavra[c] # pega a lista dentro da categoria escolhida
    indice = rdm.randint(0, len(lista_palavras_categoria) - 1) # declarando novo indice para escolher uma palavra dentro da categoria
    palavra = lista_palavras_categoria[indice] # pega a palavra dentro da lista da categoria

    tamanho = len(palavra)
    return categoria, palavra, tamanho
