# 7. Usando o exemplo anterior, adicione um método status() em Autenticacao e também em Permissao. Se a classe Administrador herda das duas, qual versão de status() será chamada? Use Administrador.__mro__ para mostrar a ordem.
class Autenticacao:
    def login(self): 
        return "LOGIN"
    def status(self):
        print("AUTENTICACAO")
class Permissao:
    def verificar_permissao(self):
        return "PERMISSAO"
    def status(self):
        print("PERMISSAO")
class Admin(Autenticacao, Permissao):
    def __init__(self):
        super().__init__()

# TESTES
# print(f"Classe: {Admin.__mro__[1].__name__}") # Mostra a versão principal de classe herdada
