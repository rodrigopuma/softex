"""1. Crie as classes Pessoa e Livro e demonstre uma relação de associação entre eles."""

class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
    def ler(self, livro):
        print(f"{self.nome} está lendo o livro {livro}.")


class Livro:
    def __init__(self, nome: str, autor: str):
        self.nome = nome
        self.autor = autor
    
    def __str__(self):
        return f"{self.nome} de {self.autor}"

p1 = Pessoa("João", 12)
livro_hp = Livro("Harry Potter", "J. K. Rowling")

p1.ler(livro_hp)
