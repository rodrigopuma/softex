


def menu():
    # barra = f'{'':-^100}'
    # print('', barra, sep='\n')
    # print(f'{'SEJA BEM-VINDO AO JOGO DA FORCA':^100}')
    # print(barra)
    pass

letra_in_palavra = lambda letra, palavra: True if letra in palavra else False

def pedir_letra():
    letra = input('Digite uma letra: ').strip().lower()
    while len(letra) > 1 or len(letra) == 0: # VALIDADOR DE OPÇÕES
        letra = input('Digite apenas uma letra: ').strip().lower()
    return letra

def indices_letra_palavra(letra, palavra, palavra_oculta=list):
    indices = []
    if not letra_in_palavra(letra, palavra):
        print(f'A letra \'{letra}\' não está na palavra.')
        vidas = -1
        
    else:
        if any(True if letras in palavra else False for letras in palavra): # Teste se a letra está na palavra com any() que retorna True se a letra estiver dentro da palavra

            for index_enumerate, letras_percorridas  in enumerate(palavra): # Se a letra tiver na palavra, ele vai percorrer novamente para verificar onde está
                if letras_percorridas == letra: # Aqui é onde ele verifica se a letra do momento é igual a letra escolhida. E pega o vetor letra da palavra pelo indice
                    
                    print(f'Boa! A letra \'{letra}\' está na palavra.') if len(indices) < 1 else None # apenas exibição

                    indices.append(index_enumerate)
                    print(f'Indices para substituir letra: {indices}')
                    vidas = 0
    
    if indices:
        for k in indices: # for para remover
            if palavra_oculta[k - 1] == '_':
                pass
            else:
                palavra_oculta.pop(k - 1)
        for i in indices: # for para adicionar
            palavra_oculta.insert(i, letra)

    return vidas, palavra_oculta
