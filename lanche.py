from abc import ABC

class Lanche(ABC):
    def __init__(self, condimento):
        self.condimento = condimento

class Hamburguer(Lanche):
    def __init__(self, carne, queijo, picles , condimento):
        super().__init__(condimento)
        self.carnes = carne
        self.queijos = queijo
        self.picles = picles

class Hot_Dog(Lanche):
    def __init__(self, proteina, molho, ovo, condimento):
        super().__init__(condimento)
        self.proteina = proteina
        self.molho = molho
        self.ovo = ovo

class Salsipao(Lanche):
    def __init__(self, condimento):
        super().__init__(condimento)