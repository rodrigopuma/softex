"""Expanda a classe Pessoa para incluir um método apresentar() que imprima uma frase como:
"Olá, meu nome é João e tenho 25 anos.". Teste o método chamando-o a partir de um objeto."""

class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
    def __str__(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}"
    
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

p1 = Pessoa("João", 25)

p1.apresentar()