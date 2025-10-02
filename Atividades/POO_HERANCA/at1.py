# 1. Crie uma classe Usuario com atributos nome e email. Depois, crie uma classe Cliente que herde de Usuario. Crie uma instancia de um cliente e acesse todos os atributos.
class Usuario():
    def __init__(self, nome: str, email: str):
        self.nome = nome
        self.email = email
    def __str__(self):
        return f"\n------------[Usuario]------------\nNome: {self.nome}\nEmail: {self.email}\n"

class Cliente(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome, email)
    def __str__(self):
        return super().__str__()

# TESTES
# client = Cliente("Rodrigo", "rodrigopuma.dev@outlook.com")
# print(client)
