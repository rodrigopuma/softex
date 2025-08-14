from functions import letra_in_palavra, pedir_letra
from arquivo import ler_palavras
vidas = 5
palavra = ''

# 1º) ESCOLHENDO PALAVRA
palavra_escolhida, tamanho = ler_palavras()

# 2º) CRIANDO UMA LISTA DE CARACTERES
PALAVRA_SEPARADA = []
for l in palavra_escolhida:
    PALAVRA_SEPARADA.append(l)



# 2º) CRIANDO PALAVRA OCULTA
palavra_oculta = []
for _ in range(tamanho):
    palavra_oculta.append('_')

print('   '.join(palavra_oculta).strip())

while True:
    quantidade = palavra_oculta.count('_') # definindo quantidade de letras na palavra oculta

    if quantidade == 0:
        print('PARABÉNS VOCÊ \033[1;33]')
    elif vidas == 0:
        break

    indices = []
    # 3º) ESCOLHENDO A LETRA
    letra_escolhida = pedir_letra()

    # 4º) VERIFICANDO SE A LETRA ESTÁ
    if not letra_in_palavra(letra_escolhida, palavra_escolhida):
        vidas -= 1
        print('VOCÊ ERROU TENTE NOVAMENTE!')
        continue

    print(f'Boa! A letra \'{letra_escolhida}\' está na palavra.')

    # 5º) PERCORRENDO A LISTA DE PALAVRA(SEPARADA) letra por letra COM ENUMERATE()
    for index_enumerate, letras_percorridas  in enumerate(PALAVRA_SEPARADA): # Se a letra tiver na palavra, ele vai percorrer novamente para verificar onde está
        if letras_percorridas == letra_escolhida: # Aqui é onde ele verifica se a letra do momento é igual a letra escolhida. E pega o vetor letra da palavra pelo indice
            indices.append(index_enumerate)
            # print(letra_escolhida)
            palavra_oculta.pop(index_enumerate)
            palavra_oculta.insert(index_enumerate, letra_escolhida)
            
            # print(f'Indices para substituir letra: {indices}')
    print(' '.join(palavra_oculta).strip())
    
    # if indices:
    #     for k in indices: # for para remover
    #         if palavra_oculta[k - 1] == '_':
    #             pass
    #         else:
    #             palavra_oculta.pop(k - 1)
    #     for i in indices: # for para adicionar
    #         palavra_oculta.insert(i, letra)


    

print('o loop encerrou')
