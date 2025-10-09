"""6. Crie a classe Casa que é composta por vários Comodos (sala, cozinha, quarto, etc.). 
Cada Comodo deve ser criado dentro da Casa."""

class Comodo:
    def __init__(self, nome_comodo):
        self.nome_comodo = nome_comodo
    def __str__(self):
        return self.nome_comodo

class Casa:
    def __init__(self, endereco: str, area: float, comodos: Comodo=None):
        self.endereco = endereco
        self.area = area
        self.comodos = [] if comodos == None else comodos

    def __str__(self):
        return f"(endereço: {self.endereco}, area em m2: {self.area})"

    def criar_comodo(self, nome_comodo):
        comodo = Comodo(nome_comodo)
        self.comodos.append(comodo)
    
    def ver_comodos(self):
        for comodo in self.comodos:
            print(comodo)

casa01 = Casa("Rua do Apolo", 200, ["Sala"])

casa01.ver_comodos()

casa01.criar_comodo("Quarto")
casa01.criar_comodo("Cozinha")

casa01.ver_comodos()