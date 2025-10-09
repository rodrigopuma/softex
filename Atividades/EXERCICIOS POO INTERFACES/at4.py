"""4. Forçando contrato

Crie uma interface Repositorio com os métodos salvar(objeto) e buscar(id). 
Depois, crie uma classe RepositorioMemoria que não implemente um dos métodos. 
O que acontece quando você tenta instanciá-la? Corrija o código."""

from abc import ABC, abstractmethod

class Repositorio(ABC):
    @abstractmethod
    def salvar(self, objeto): ...

    @abstractmethod
    def buscar(self, id): ...

class RepositorioMemoria(Repositorio):
    def salvar(self, objeto):
        return super().salvar(objeto)

try:
    rep_mem = RepositorioMemoria()
except TypeError:
    print("Não é possivel instanciar um objeto na classe RepositorioMemoria, pois há um metódo abstrato herdado que não está implementado")

# Corrigindo

class RepositorioMemoria(Repositorio):
    def salvar(self, objeto):
        print(f"{objeto} salvo na memoria do repositorio")
        return super().salvar(objeto)
    def buscar(self, id):
        print(f"{id} encontrado na memoria do repositorio")
        return super().buscar(id)

rep_mem = RepositorioMemoria()
rep_mem.salvar("objeto")