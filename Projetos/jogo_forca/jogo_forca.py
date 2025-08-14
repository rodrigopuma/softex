from functions import menu, escolher_palavra, pedir_letra, indices_letra_palavra

vidas = 4

menu()



palavra_escolhida, tamanho_palavra = escolher_palavra()

# tracos = (' _ ' * tamanho_palavra).strip() # fazer com lista
palavra_oculta = []
for _ in range(tamanho_palavra):
    palavra_oculta.append('_')
print(palavra_oculta)
quantidade = palavra_oculta.count('_')
print(palavra_oculta.index('_', 0, quantidade))

while True:

    letra_escolhida = pedir_letra()
    if indices_letra_palavra(letra_escolhida, palavra_escolhida, vidas) == -1:
        vidas -= 1
    else:
        pass
    print(f'Vidas: {vidas}')
