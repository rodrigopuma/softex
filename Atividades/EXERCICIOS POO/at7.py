"""Crie uma classe Aluno com atributos nome e nota. Depois crie uma classe Turma que tenha uma lista de alunos e um método adicionar_aluno(aluno). 
Crie alguns objetos Aluno e adicione-os à turma."""

class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

class Turma:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_alunos(self):
        for aluno in self.alunos: 
            print(f"Nome: {aluno.nome}, Nota: {aluno.nota}")

turma = Turma()

aluno1 = Aluno("João", 10)
aluno2 = Aluno("Maria", 8)
aluno3 = Aluno("Pedro", 9)

turma.adicionar_aluno(aluno1)