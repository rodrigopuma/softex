"""Na classe Aluno, implemente o método __str__ para que, ao imprimir um objeto da classe, apareça algo como:"Aluno: Maria - Nota: 9.5". Teste imprimindo os objetos."""

class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def __str__(self):
        return f"Aluno: {self.nome} - Nota: {self.nota}"
    
aluno1 = Aluno("João", 10)
aluno2 = Aluno("Maria", 8)

print(aluno1)
print(aluno2)