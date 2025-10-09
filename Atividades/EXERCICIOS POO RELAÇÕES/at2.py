"""2. Crie as classes Aluno e Onibus. Crie um método em Aluno que use a classe Onibus."""

from datetime import datetime as dt

class Onibus:
    def __init__(self, nome_linha: str, numero_linha: int, numero_carro: int):
        self.nome_linha = nome_linha
        self.numero_linha = numero_linha
        self.numero_carro = numero_carro

class Aluno:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
    
    def pegar_onibus(self, onibus: Onibus):
        print(f"{self.nome} pegou o ônibus da linha {onibus.numero_linha} às {dt.now().strftime('%H:%M')}")

onibus_2920 = Onibus("Rio Doce / CDU", 2920, 2931)
estudante = Aluno("Guilherme", 14)

estudante.pegar_onibus(onibus_2920)
