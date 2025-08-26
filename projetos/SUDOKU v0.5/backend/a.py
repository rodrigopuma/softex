import json
ARQUIVO = './backend/jogo.json'

NUMEROS = (1, 2, 3, 4, 5, 6, 7, 8, 9)
LISTA_OBJ = [n for n in range(1, 82)]
jogo = [[]]
lista_temp = []

igual = lambda v1, v2: True if v1 == v2 else False 



for i in LISTA_OBJ:
    lista_temp.append(id(i))
    
    if igual(i, 9) or igual(i, 18) or igual(i, 27) or igual(i, 36) or igual(i, 45) or igual(i, 54) or igual(i, 63) or igual(i, 72) or igual(i, 81):
        jogo.extend(lista_temp)
        # with open(ARQUIVO, 'a', encoding='utf-8') as arquivo:
        #     json.dump(lista_temp, arquivo, indent=4, ensure_ascii=False)
        lista_temp.clear()
with open(ARQUIVO, 'r', encoding='utf-8') as arch:
    lista = json.load(arch)

for k, j in enumerate(lista):
    print(f'{k}: {j}')