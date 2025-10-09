"""Herança parcial

Crie uma classe abstrata Transporte com dois métodos abstratos: 
mover() e parar(). Depois, crie uma subclasse Carro que implemente apenas o método mover(). 
O que acontece quando você tenta instanciar Carro? Corrija implementando o segundo método."""

from abc import ABC, abstractmethod

class Transporte(ABC):
    @abstractmethod
    def mover(self, metros): ...

    @abstractmethod
    def parar(self): ...

class Carro(Transporte):
    def mover(self, metros: float):
        return f"O carro moveu {metros} metros"

try:    
    car = Carro()
    car.mover(30)
except TypeError:
    print("Não é possivel instanciar um objeto na classe Carro, pois há um metódo abstrato herdado que não está implementado")

# Corrigindo

class Carro(Transporte):
    def mover(self, metros: float):
        return f"O carro moveu {metros} metros"
    def parar(self):
        return super().parar()

car = Carro()
car.mover(30)