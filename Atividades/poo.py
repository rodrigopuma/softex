class Animal:
    def __init__(self, nome:str, especie:str, raca:str, idade:int):
        self.nome = nome
        self.especie = especie
        self.raca = raca
        self.idade = idade
    
    def __str__(self):
        return f"Nome: {self.nome}\nEspécie: {self.especie}\nRaça: {self.raca}\nIdade: {self.idade}"

class Dono:
    def __init__(self, cpf, nome, celular="81999999"):
        self.cpf = cpf
        self.nome = nome
        self.celular = celular
        self.contas_pagar = []

class PetShop:
    def __init__(self, animais=[]):
        self.animais = animais
    
    def listar_animais(self):
        for animal in self.animais:
            print('-'*100, animal, '-'*100, sep='\n')

    def add_animal(self, obj):
        self.animais.append(obj)

    def buscar_animal(self, nome="", especie=""):
        if nome == "" and especie == "":
            raise ValueError("O metodo precisa de pelo menos um dos parâmetros")
        else:
            for contador_geral, animal in enumerate(self.animais, start=0):
                if (animal.nome.lower() == nome.lower()) or (animal.especie.lower() == especie.lower()): # Verifica se o animal está
                    contador_geral += 1
                    print(animal)
                    print('-'*100, '-'*100, sep='\n')
            if contador_geral > 1:
                for contador, animal in enumerate(self.animais, start=0):
                    if (animal.nome.lower() == nome.lower()) or (animal.especie.lower() == especie.lower()): # Verifica se o animal está
                        if not (animal.nome.lower() == nome.lower()) and not (animal.especie.lower() == especie.lower()):
                            raise ValueError("Não tem nenhum animal com esse nome e especie verifique se você digitou corretamente as duas informações")
                        else:
                            if contador < 1:
                                contador = 1
                                print(f"Foram encontrados {contador_geral} animais com essas informações, segue abaixo todos eles:\nAnimal {contador}:\n{animal}")
                            else:
                                contador += 1
                                print(f"\nAnimal {contador}\n{animal}")



    def remover_animal(self, nome: str):
        for animal in self.animais:
            if animal.nome.lower() == nome.lower():
                self.animais.remove(animal)
            else: pass


clinica = PetShop()
shitzu = Animal("Rex", "Cachorro", "Shitzu", 12)
maine_coon = Animal("Mimi", "Gato", "Maine Coon", 2)
papagaio = Animal("Tico", "Pássaro", "Papagaio", 34)

clinica.add_animal(shitzu)
clinica.add_animal(maine_coon)
clinica.add_animal(papagaio)


clinica.buscar_animal("Rex")

