"""3. Crie uma classe Funcionario e Departamento que contém uma lista de Funcionarios.
Departamento deve agregar funcionários já criados."""

class Funcionario:
    def __init__(self, nome: str):
        self.nome = nome
    def __str__(self):
        return f"nome: {self.nome}"

class Departamento:
    def __init__(self, nome_dp):
        self.nome_dp = nome_dp
        self.funcionarios = []

    def criar_funcionario(self, nome):
        colab = Funcionario(nome)
        self.funcionarios.append(colab)
    
    def ver_funcionarios(self):
        for colab in self.funcionarios:
            print(f"{colab}")


ti = Departamento("Tecnologia")

ti.criar_funcionario("Rodrigo")
ti.criar_funcionario("Fred")
ti.ver_funcionarios()