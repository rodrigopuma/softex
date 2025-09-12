"""Crie uma classe, Pessoa, que tenha os atributos: nome, data de nascimento, cpf, identidade. 
Deixe os atributos cpf e identidade como privado e monte os métodos setters e getters para acessar e editar os valores"""

class Pessoa:
    def __init__(self, nome: str, data_nascimento: str, cpf: int, rg: int):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.__cpf = cpf
        self.__rg = rg
    
    def get_atribute(self, name: str):
        if name.lower() == "cpf":
            return int(self.__cpf)
        elif name.lower() == "rg":
            return int(self.__rg)
        else:
            print("Opção inválida selecione [\"rg\" ou \"cpf\"]")
            return False
        
    def set_atribute(self, name: str, value: int=None):
        if value is None:
            if name.lower() == "cpf":
                self.__cpf = int(input("Digite seu CPF sem pontuações: "))
            elif name.lower() == "rg":
                self.__rg = int(input("Digite seu RG sem pontuações: "))
        else:
            if name.lower() == "cpf":
                self.__cpf = value
            elif name.lower() == "rg":
                self.__rg = value

