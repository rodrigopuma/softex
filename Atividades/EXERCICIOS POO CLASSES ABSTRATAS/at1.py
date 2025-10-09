"""1. Definição de classe abstrata
Crie uma classe abstrata chamada Animal que possua um método abstrato falar(). 
Em seguida, crie duas classes concretas (Cachorro e Gato) que implementem esse método. 
Mostre o uso criando objetos e chamando o método falar()."""

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def falar(self): ...

class Cachorro(Animal):
    def falar(self):
        return "au au"

class Gato(Animal):
    def falar(self):
        return "miau"

# animal = Animal() # isso gera um erro de instanciamento
dog = Cachorro()
print(dog.falar())

cat = Gato()
print(cat.falar())
