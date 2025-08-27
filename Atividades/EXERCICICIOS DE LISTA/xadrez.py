tabuleiro = [[linha for linha in range(8)] for _ in range(8)]

# tabuleiro_zeros = np.zeros((8, 8))

for n_linha, linha in enumerate(tabuleiro, start=1):
    if n_linha == 1 or n_linha == 8:
        tabuleiro[n_linha - 1].insert(0, 'tor'), tabuleiro[n_linha - 1].remove(0) # adicionando torre na primeira casa da primeira e ultima linha
        tabuleiro[n_linha - 1].insert(1, 'cav'), tabuleiro[n_linha - 1].remove(1) # adicionando cavalo na segunda casa da primeira e ultima linha
        tabuleiro[n_linha - 1].insert(2, 'bis'), tabuleiro[n_linha - 1].remove(2) # adicionando bispo na terce
        tabuleiro[n_linha - 1].insert(3, 'rai'), tabuleiro[n_linha - 1].remove(3)
        tabuleiro[n_linha - 1].insert(4, 'rei'), tabuleiro[n_linha - 1].remove(4)
        tabuleiro[n_linha - 1].insert(5, 'bis'), tabuleiro[n_linha - 1].remove(5) # adicionando bispo na terce
        tabuleiro[n_linha - 1].insert(6, 'cav'), tabuleiro[n_linha - 1].remove(6) # adicionando cavalo na segunda casa da primeira e ultima linha
        tabuleiro[n_linha - 1].insert(7, 'tor'), tabuleiro[n_linha - 1].remove(7) # adicionando torre na primeira casa da primeira e ultima linha
    
    elif n_linha == 2 or n_linha == 7:
        linha.clear()
        for _ in range(8):
            linha.append('pea')

    else:
        linha.clear()
        for _ in range(8):
            linha.append([])

# print(len(tabuleiro))
# print('\033[1;32m')
for linha in tabuleiro:
    for casas in linha:
        if casas == 'tor':
            print(f'\033[1;31m{casas}\033[m', end=' ')
        elif casas == 'cav':
            print(f'\033[1;30m{casas}\033[m', end=' ')
        elif casas == 'bis':
            print(f'\033[1;33m{casas}\033[m', end=' ')
        elif casas == 'rai':
            print(f'\033[1;35m{casas}\033[m', end=' ')
        elif casas == 'rei':
            print(f'\033[1;36m{casas}\033[m', end=' ')
        elif casas == 'pea':
            print(f'\033[7;30;40m{casas}\033[m', end=' ')
        else:
            print(casas, end='  ')
    print()
    # print(len(linha))


# for n_linha, linha in enumerate(list(tabuleiro_zeros), start=1):
#     if n_linha == 1 or n_linha == 8:
#         for n_casas, casas in enumerate(linha, start=1):
#             if n_casas == 1 or n_casas == 8:
#                 print(tabuleiro_zeros[n_linha - 1])
#                 np.insert(tabuleiro_zeros, [n_casas], 5)
#                 print(tabuleiro_zeros)