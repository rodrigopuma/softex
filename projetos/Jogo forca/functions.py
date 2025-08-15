def menu():
    barra = f'{'':-^100}'
    print('', barra, sep='\n')
    print(f'{'SEJA BEM-VINDO AO JOGO DA FORCA':^100}')
    print(barra)

letra_in_palavra = lambda letra, palavra: True if letra in palavra else False

def pedir_letra():
    letra = input('Digite uma letra: ').strip().lower()
    while len(letra) > 1 or len(letra) == 0: # VALIDADOR DE OPÇÕES
        letra = input('Digite apenas uma letra: ').strip().lower()
    return letra

