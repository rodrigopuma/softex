"""1. Criando uma interface

Crie uma interface chamada Pagamento com um método abstrato processar(valor). 
Depois, crie duas classes (CartaoCredito e Boleto) que implementem a interface. 
Mostre como chamar processar() para cada uma."""

from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def processar(self, valor): ...

class CartaoCredito(Pagamento):
    def processar(self, valor, parcelas):
        return f"Processando R${valor} em {parcelas}x"
    
class BoletoBancario(Pagamento):
    def processar(self, valor):
        return f"Processando R${valor}. O pagamento deve cair em até 3 dias úteis"

cartao = CartaoCredito()
boleto = BoletoBancario()

print(cartao.processar(1200, 12), boleto.processar(500), sep="\n")