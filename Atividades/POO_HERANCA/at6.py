# 6. Crie uma classe Autenticacao com um método login(). Crie outra classe Permissao com um método verificar_permissao(). Em seguida, crie uma classe Administrador que herda de ambas. Como usar os métodos herdados?
class Autenticacao:
    def login(self): 
        return "LOGIN"
class Permissao:
    def verificar_permissao(self):
        return "PERMISSAO"
class Admin(Autenticacao, Permissao):
    def __init__(self):
        super().__init__()

# TESTES
# admin01 = Admin()
# print(admin01.login())
# print(admin01.verificar_permissao())
