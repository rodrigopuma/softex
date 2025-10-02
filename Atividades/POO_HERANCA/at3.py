# 3. Na classe Usuario, crie um método saudacao() que retorna "Olá, usuário". Na classe Cliente, sobrescreva esse método para retornar "Olá, cliente". Mostre como funciona a chamada.
class Usuario():
    def __init__(self, nome: str, email: str):
        self.nome = nome
        self.email = email

    def __str__(self):
        return f"\n------------[Usuario]------------\nNome: {self.nome}\nEmail: {self.email}\n"
        
    def exibir_informacoes(self):
        print(f"ID_TEMP: {id(self)}\nNome: {self.nome}\nEmail: {self.email}")
        
    def saudacao(self):
        return "Olá, usuário"

class Cliente(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome, email)
    def __str__(self):
        return super().__str__()
    def saudacao(self):
        return "Olá, cliente"

# TESTES
# client = Cliente("Rodrigo", "rodrigopuma.dev@outlook.com")
# print(client.saudacao())
