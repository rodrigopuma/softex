"""Crie uma classe Cachorro com um atributo de classe especie = "Canis familiaris" e atributos de instância nome e idade. 
Mostre a diferença entre acessar especie pelo objeto e pela classe."""

class Cachorro:
    especie = "Canis familiaris"
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.especie = "Canis"

    def __str__(self):
        return f"{self.nome} é um cachorro da espécie {self.especie} e tem {self.idade} anos."
    
cachorro1 = Cachorro("Bolinha", 3)
print(Cachorro.especie)
print(cachorro1.especie)