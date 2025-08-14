import json
import random as rdm

ARQUIVO_PALAVRAS = './palavras.json'

def ler_palavras():
    """
    Le as palavras dentro do arquivo escolhe uma aleatoriamente

    retorna a (palavra e o tamanho dela)
    """
    with open(ARQUIVO_PALAVRAS, 'r', encoding='utf-8') as arquivo:
        lista_palavras = list(json.load(arquivo))
    indice = rdm.randint(0, (len(lista_palavras) - 1))
    palavra_escolhida = lista_palavras[indice]
    tamanho = len(palavra_escolhida)
    return palavra_escolhida, tamanho