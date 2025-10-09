"""Múltiplos métodos abstratos

Defina uma classe abstrata FormaGeometrica com dois métodos abstratos: 
area() e perimetro(). Crie uma classe concreta Retangulo que herde de FormaGeometrica
e implemente os dois métodos. Teste criando um objeto e calculando sua área e perímetro."""

from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    @abstractmethod
    def area(self): ...

    @abstractmethod
    def perimetro(self): ...

class Retangulo(FormaGeometrica):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return (self.base * 2) + (self.altura * 2)
    
retangulo = Retangulo(5, 8)
print(f"Area: {retangulo.area()}\nPerimetro: {retangulo.perimetro()}")