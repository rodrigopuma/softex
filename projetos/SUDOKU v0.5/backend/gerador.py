import json

def criar_base_jogo(ARQUIVO='./jogo.json'): 
    with open(ARQUIVO, 'r', encoding='utf-8') as archive:
        jogo = json.load(archive)
    return jogo

def gerar_tabuleiro(dificuldade: str= "facil"):
    """Gera uma matriz de 9x9 com alguns números preenchidos conforme dificuldade
    (facil, medio, dificil)

    Args:
        dificuldade (str): alguma dificuldade como facil, medio ou dificil

    Returns:
        list[list[int]]: Uma matriz de 9x9
    """
    from random import randint
    
    base_jogo = criar_base_jogo()
    tabuleiro = []
    numeros_temp = []

    # Listas separadas por blocos


    primeiro_bloco = [base_jogo[0][0:3], base_jogo[1][0:3], base_jogo[2][0:3]]
    segundo_bloco = [base_jogo[0][3:6], base_jogo[1][3:6], base_jogo[2][3:6]]
    terceiro_bloco = [base_jogo[0][6:10], base_jogo[1][6:10], base_jogo[2][6:10]]

    quarto_bloco = [base_jogo[3][0:3], base_jogo[4][0:3], base_jogo[5][0:3]]
    quinto_bloco = [base_jogo[3][3:6], base_jogo[4][3:6], base_jogo[5][3:6]]
    sexto_bloco = [base_jogo[3][6:10], base_jogo[4][6:10], base_jogo[5][6:10]]

    setimo_bloco = [base_jogo[6][0:3], base_jogo[7][0:3], base_jogo[8][0:3]]
    oitavo_bloco = [base_jogo[6][3:6], base_jogo[7][3:6], base_jogo[8][3:6]]
    nono_bloco = [base_jogo[6][6:10], base_jogo[7][6:10], base_jogo[8][6:10]]
    
    primeiro_bloco.clear(), segundo_bloco.clear(), terceiro_bloco.clear(), quarto_bloco.clear(), quinto_bloco.clear(), sexto_bloco.clear(), setimo_bloco.clear(), oitavo_bloco.clear(), nono_bloco.clear()
    
    primeiro_bloco.extend(base_jogo[0][0:3]), primeiro_bloco.extend(base_jogo[1][0:3]), primeiro_bloco.extend(base_jogo[2][0:3])
    segundo_bloco.extend(base_jogo[0][3:6]), segundo_bloco.extend(base_jogo[1][3:6]), segundo_bloco.extend(base_jogo[2][3:6])
    terceiro_bloco.extend(base_jogo[0][6:10]), terceiro_bloco.extend(base_jogo[1][6:10]), terceiro_bloco.extend(base_jogo[2][6:10])

    quarto_bloco.extend(base_jogo[3][0:3]), quarto_bloco.extend(base_jogo[4][0:3]), quarto_bloco.extend(base_jogo[5][0:3])
    quinto_bloco.extend(base_jogo[3][3:6]), quinto_bloco.extend(base_jogo[4][3:6]), quinto_bloco.extend(base_jogo[5][3:6])
    sexto_bloco.extend(base_jogo[3][6:10]), sexto_bloco.extend(base_jogo[4][6:10]), sexto_bloco.extend(base_jogo[5][6:10])

    setimo_bloco.extend(base_jogo[6][0:3]), setimo_bloco.extend(base_jogo[7][0:3]), setimo_bloco.extend(base_jogo[8][0:3])
    oitavo_bloco.extend(base_jogo[6][3:6]), oitavo_bloco.extend(base_jogo[7][3:6]), oitavo_bloco.extend(base_jogo[8][3:6])
    nono_bloco.extend(base_jogo[6][6:10]), nono_bloco.extend(base_jogo[7][6:10]), nono_bloco.extend(base_jogo[8][6:10])

    for i, l in enumerate(base_jogo):
        print(f'{i}: {l}')

    print('-' * 100)

    for linha in base_jogo:
        while len(numeros_temp) < 9:
            numero_aleatorio = randint(1, 9)
            
            if numero_aleatorio in numeros_temp:
                pass
            else:
                numeros_temp.append(numero_aleatorio)
            
        print('-' * 100)
        print(numeros_temp)
        tabuleiro.append(numeros_temp[:])
        numeros_temp.clear()
        
    for l in tabuleiro:
        print(l)
        # for _ in range(9):
        #     numero_aleatorio = randint(1, 9)
        #     lista_temp.insert(randint(0, 8), numero_aleatorio if numero_aleatorio not in lista_temp else numero_aleatorio)
        # não pode repetir na mesma linha
        # pass
    # return list[list[int]]