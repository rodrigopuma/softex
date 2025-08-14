import json
import random as rdm

ARQUIVO_PALAVRAS = './palavras.json'

def menu():
    barra = f'{'':-^100}'
    print('', barra, sep='\n')
    print(f'{'SEJA BEM-VINDO AO JOGO DA FORCA':^100}')
    print(barra)
    letra_in_palavra = lambda letra, palavra: True if letra in palavra else False

def pedir_letra():
    letra = input('Digite uma letra: ').strip().lower()
    while len(letra) > 1:
        letra = input('Digite apenas uma letra: ').strip().lower()
    return letra

def escolher_palavra():
    with open(ARQUIVO_PALAVRAS, 'r', encoding='utf-8') as arquivo:
        lista_palavras = list(json.load(arquivo))
        print(lista_palavras)
    indice = rdm.randint(0, (len(lista_palavras) + 1))
    palavra_escolhida = lista_palavras[indice-1]
    tamanho = len(palavra_escolhida)
    return palavra_escolhida, tamanho

letra_in_palavra = lambda letra, palavra: True if letra in palavra else False


def indices_letra_palavra(letra, palavra, vidas):
    indices = []
    if not letra_in_palavra(letra, palavra):
        print(f'A letra \'{letra}\' não está na palavra.')
        vidas = -1
        
    else:
        if any(True if letras in palavra else False for letras in palavra): # Teste se a letra está na palavra com any() que retorna True se a letra estiver dentro da palavra

            for letras_percorridas in palavra: # Se a letra tiver na palavra, ele vai percorrer novamente para verificar onde está

                if letras_percorridas == letra: # Aqui é onde ele verifica se a letra do momento é igual a letra escolhida. E pega o vetor letra da palavra pelo indice
                    
                    print(f'Boa! A letra \'{letra}\' está na palavra.') if len(indices) < 1 else None # apenas exibição

                    indices.append(palavra.index(letras_percorridas))
                    print(f'Indices para substituir letra: {indices}')
                    vidas = 0
    return vidas

            