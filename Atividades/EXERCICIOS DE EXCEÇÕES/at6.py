"""Crie uma exceção personalizada chamada IdadeInvalidaError. 
Depois, crie uma função cadastrar_idade(idade) que lance essa exceção caso a idade seja negativa."""

class IdadeInvalidaError(Exception): ...

def cadastrar_idade(idade: int):
    try:
        idade
        if idade < 0:
            raise IdadeInvalidaError("A idade não pode ser negativa")
        elif idade == 0:
            raise IdadeInvalidaError("A idade não pode ser 0")
    except IdadeInvalidaError as erro:
        print(f"{type(erro).__name__}: {erro}")
        return False
    else:
        print("Idade cadastrada com sucesso.")
        return True

cadastrar_idade(0)
cadastrar_idade(-1)

