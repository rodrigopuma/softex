"""4. Crie as classes Time e Jogador. Um Jogador tem nome e posição como atributos, 
enquanto Time agrega jogadores em uma lista."""

class Jogador:
    def __init__(self, nome: str, posicao: str, nome_time: str):
        self.nome = nome
        self.posicao = posicao
        self.time = nome_time
    def __str__(self):
        return f"(nome: {self.nome}, posição: {self.posicao}, nome do time: {self.time})"

class Time:
    def __init__(self, nome_time: str, elenco: list=None):
        self.nome_time = nome_time
        self.elenco = [] if elenco == None else elenco

    def adicionar_jogador(self, nome, posicao):
        jogador = Jogador(nome, posicao, self.nome_time)
        self.elenco.append(jogador)
    
    def ver_elenco(self):
        for jogador in self.elenco:
            print(f"{jogador}")

psg = Time("PSG", [Jogador("Neymar", "PE", "PSG"), Jogador("Mbappe", "ATA", "PSG"), Jogador("Messi", "PD", "PSG")])

psg.adicionar_jogador("Verrati", "MC")

psg.ver_elenco()
