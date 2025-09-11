"""Usando a classe Carro, crie um objeto e depois altere o valor de um de seus atributos (por exemplo, mudar o ano). Imprima antes e depois da alteração."""

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def __str__(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}"

mustang = Carro("Chevrolet", "Mustang", "2018")
print(mustang)
mustang.ano = "2022"
print(mustang)