"""5. Crie a classe Carro que possui um Motor. 
O Motor deve ser criado dentro do Carro. 
Se o Carro deixar de existir, o Motor também deixa. 
Mostre isso criando e depois apagando o objeto."""

class Motor:
    def __init__(self, potencia: int):
        self.potencia = potencia

    def ligar(self):
        print(f"Motor de {self.potencia} cavalos ligado.")

class Carro:
    def __init__(self, modelo: str, potencia_motor: int):
        self.modelo = modelo
        self.motor = Motor(potencia_motor)
    
    def ligar(self):
        print(f"Ligando o carro {self.modelo}")
        self.motor.ligar()

punto = Carro("Punto", 150)
punto.ligar()

del punto # o motor do punto nao existe mais
