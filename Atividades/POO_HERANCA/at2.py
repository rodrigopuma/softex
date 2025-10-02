# 2. Implemente um método exibir_informacoes() na classe Usuario e herde esse método em Cliente. Mostre como chamar o método herdado a partir de um objeto Cliente.
class Usuario():
    def __init__(self, nome: str, email: str):
        self.nome = nome
        self.email = email
    def __str__(self):
        return f"\n------------[Usuario]------------\nNome: {self.nome}\nEmail: {self.email}\n"
    def exibir_informacoes(self):
        print(f"ID_TEMP: {id(self)}\nNome: {self.nome}\nEmail: {self.email}")

class Cliente(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome, email)
    def __str__(self):
        return super().__str__()

# TESTES
# client = Cliente("Rodrigo", "rodrigopuma.dev@outlook.com")
# client.exibir_informacoes()
