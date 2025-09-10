"""Crie uma classe chamada Pessoa que tenha os atributos nome e idade. Em seguida, crie dois objetos dessa classe e imprima os valores de seus atributos."""

class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
    def __str__(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}"

p1 = Pessoa("Roberto", 56)
p2 = Pessoa("Maria", 42)

print(p1, p2, sep=f'\n{'-' * 100}\n')