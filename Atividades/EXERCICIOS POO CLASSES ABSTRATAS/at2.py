"""2. Proibição de instanciamento

Tente instanciar diretamente a classe Animal da questão anterior e explique o erro gerado pelo Python."""

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def falar(self): ...

try:
    animal = Animal()
except TypeError:
    print("Não é possivel instanciar um objeto na classe Animal, pois ela é uma classe abstrata.")