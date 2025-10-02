# 4. Na classe Cliente, adicione o atributo saldo. Adicione um método construtor em Cliente que inicialize também os atributos de Usuario usando super().
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
    def __init__(self, nome, email, saldo: float):
        super().__init__(nome, email)
        self.saldo = saldo
    def __str__(self):
        return f"\n------------[Cliente]------------\nNome: {self.nome}\nEmail: {self.email}\nSaldo: R${self.saldo}\n"
    def saudacao(self):
        return "Olá, cliente"
