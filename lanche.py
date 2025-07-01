from abc import ABC
from implementacao import *


class Lanche(ABC):
    def __init__(self, carne: Carne, condimento: Condimento):
        self.carne = carne
        self.condimento = condimento

    def preparar(self):
        pass

class Hamburguer(Lanche):
    def __init__(self, carne: Carne, queijo, picles, condimento: Condimento):
        super().__init__(carne, condimento)
        self.carne = carne
        self.queijo = queijo
        self.picles = picles

    def preparar(self):
        return f"Hambúrguer {self.carne.grelhar()} com {self.queijo}, {self.picles} e {self.condimento.adicionar()}"

class Salchipao(Lanche):
    def __init__(self, carne: Carne, molho, ovo, condimento: Condimento):
        super().__init__(carne, condimento)
        self.carne = carne
        self.molho = molho
        self.ovo = ovo

    def preparar(self):
        return f"Salchipão {self.carne.grelhar()} com {self.molho}, ovo e {self.condimento.adicionar()}"