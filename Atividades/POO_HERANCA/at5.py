# 5. Crie uma classe Funcionario que herda de Usuario e, em seguida, crie uma classe Gerente que herda de Funcionario. Mostre como instanciar um gerente e acessar seus atributos.
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
    
class Funcionario(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome, email)
class Gerente(Funcionario):
    def __init__(self, nome, email):
        super().__init__(nome, email)
gerente01 = Gerente("Rodrigo", "rodrigopuma.dev@outlook.com")
