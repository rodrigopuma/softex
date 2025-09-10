"""Crie uma classe Carro com os atributos marca, modelo e ano. Use o método __init__ para inicializar esses valores. Crie três objetos e mostre suas informações."""

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def __str__(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}"
    
mustang = Carro("Chevrolet", "Mustang", "2018")
corolla = Carro("Toyota", "Corolla", "2022")
byd = Carro("BYD", "Song Plus", "2024")

print(mustang, corolla, byd, sep=f"\n{'-'*100}\n")