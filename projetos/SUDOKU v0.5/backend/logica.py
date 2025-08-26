import json

NUMEROS = (1, 2, 3, 4, 5, 6, 7, 8, 9)
LISTA_OBJ = [n for n in range(1, 82)]
lista_temp = []

def criar_base_jogo(ARQUIVO='./jogo.json'):
    with open(ARQUIVO, 'r', encoding='utf-8') as archive:
        jogo = json.load(archive)
    return jogo

def gerar_tabuleiro(dificuldade: str):
    """Gera uma matriz de 9x9 com alguns números preenchidos conforme dificuldade
    (facil, medio, dificil)

    Args:
        dificuldade (str): alguma dificuldade como facil, medio ou dificil

    Returns:
        list[list[int]]: Uma matriz de 9x9
    """
    jogo = criar_base_jogo()
    numeros_temp = []

    # Listas separadas por blocos


    primeiro_bloco = [jogo[0][0:3], jogo[1][0:3], jogo[2][0:3]]
    segundo_bloco = [jogo[0][3:6], jogo[1][3:6], jogo[2][3:6]]
    terceiro_bloco = [jogo[0][6:10], jogo[1][6:10], jogo[2][6:10]]

    quarto_bloco = [jogo[3][0:3], jogo[4][0:3], jogo[5][0:3]]
    quinto_bloco = [jogo[3][3:6], jogo[4][3:6], jogo[5][3:6]]
    sexto_bloco = [jogo[3][6:10], jogo[4][6:10], jogo[5][6:10]]

    setimo_bloco = [jogo[6][0:3], jogo[7][0:3], jogo[8][0:3]]
    oitavo_bloco = [jogo[6][3:6], jogo[7][3:6], jogo[8][3:6]]
    nono_bloco = [jogo[6][6:10], jogo[7][6:10], jogo[8][6:10]]
    
    primeiro_bloco.clear(), segundo_bloco.clear(), terceiro_bloco.clear(), quarto_bloco.clear(), quinto_bloco.clear(), sexto_bloco.clear(), setimo_bloco.clear(), oitavo_bloco.clear(), nono_bloco.clear()
    
    primeiro_bloco.extend(jogo[0][0:3]), primeiro_bloco.extend(jogo[1][0:3]), primeiro_bloco.extend(jogo[2][0:3])
    segundo_bloco.extend(jogo[0][3:6]), segundo_bloco.extend(jogo[1][3:6]), segundo_bloco.extend(jogo[2][3:6])
    terceiro_bloco.extend(jogo[0][6:10]), terceiro_bloco.extend(jogo[1][6:10]), terceiro_bloco.extend(jogo[2][6:10])

    quarto_bloco.extend(jogo[3][0:3]), quarto_bloco.extend(jogo[4][0:3]), quarto_bloco.extend(jogo[5][0:3])
    quinto_bloco.extend(jogo[3][3:6]), quinto_bloco.extend(jogo[4][3:6]), quinto_bloco.extend(jogo[5][3:6])
    sexto_bloco.extend(jogo[3][6:10]), sexto_bloco.extend(jogo[4][6:10]), sexto_bloco.extend(jogo[5][6:10])

    setimo_bloco.extend(jogo[6][0:3]), setimo_bloco.extend(jogo[7][0:3]), setimo_bloco.extend(jogo[8][0:3])
    oitavo_bloco.extend(jogo[6][3:6]), oitavo_bloco.extend(jogo[7][3:6]), oitavo_bloco.extend(jogo[8][3:6])
    nono_bloco.extend(jogo[6][6:10]), nono_bloco.extend(jogo[7][6:10]), nono_bloco.extend(jogo[8][6:10])

    for i, k in enumerate(jogo):
        print(f'{i}: {k}')

    print('-' * 100)
    print(primeiro_bloco)
    print(segundo_bloco)

    for linha in jogo:
        # não pode repetir na mesma linha
        pass
    # return list[list[int]]

def validar_jogada(
        tabuleiro: list[list[int]], linha: int,
        coluna: int, numero: int
        ):
    """_summary_

    Args:
        tabuleiro (list[list[int]]): _description_
        linha (int): _description_
        coluna (int): _description_
        numero (int): _description_

    Returns:
        bool: _description_
    """
    return bool

gerar_tabuleiro("")