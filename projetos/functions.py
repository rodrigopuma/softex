import random as rdm

def gerar_jogo():
    """Gerar 9 vetores sorteados para montar dentro da matriz
    sem repetir numero dentro dentro de cada vetor
    """
    for _ in range(9):
        lista_num_aleatorios = set()
        for i in range(1, 10):
            lista_num_aleatorios.add(i)
        
    print(lista_num_aleatorios)        # for v in 

gerar_jogo()