matriz = [
    # Linhas na verdade
    [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]], # 1º Vetor
    [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]], # 2º Vetor
    [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]], # 3º Vetor

    [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]], # 4º Vetor
    [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]], # 5º Vetor
    [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]], # 6º Vetor

    [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]], # 7º Vetor
    [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]], # 8º Vetor
    [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]], # 9º Vetor
    ]

# MATRIZ [] BRANCO
# VETOR [] ROSA
# LINHA [] AZUL

# EXIBIÇÃO
for contador_vetor, v in enumerate(matriz, start=1): # vai percorrer a matriz completa voltando com os vetores
    print(f'{contador_vetor}º Vetor:')
    print('[',end=' ')
    for contador_linhas, linhas in enumerate(v, start=1): # aqui ele vai percorrer as linhas dos vetores retornando com as linhas de cada um
        print(f'{contador_linhas}ª linha: ', end=' ')
        print(linhas, end='      ') if contador_linhas < 3 else print(linhas, end=' ') # vai printar todas as linhas das do vetor escolhido logo
        # FAZER MELHORIAS PARA PERCORRER LINHAS DE UMA FORMA MAIS FACIL
    print(']', end='\n\n')
    
    # print(v)
    if contador_vetor % 3 == 0:
        print('')
