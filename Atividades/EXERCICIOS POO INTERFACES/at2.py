"""2. Interface múltipla

Crie duas interfaces: Ligavel (com o método ligar()) e Desligavel (com o método desligar()). 
Crie uma classe Computador que implemente ambas. Mostre seu uso."""

from abc import ABC, abstractmethod

class Ligavel(ABC):
    @abstractmethod
    def ligar(self): ...

class Desligavel(ABC):
    @abstractmethod
    def desligar(self): ...

class Computador(Ligavel, Desligavel):
    def ligar(self):
        print("Ligando computador")
    def desligar(self):
        print("Desligando computador")

pc = Computador()
pc.ligar()