from abc import ABC, abstractmethod
from implementacao import *


class Lanche(ABC):
    def __init__(self, carne: Carne, condimento: Condimento):
        self.carne = carne
        self.condimento = condimento

    @abstractmethod
    def preparar(self):
        pass

class Hamburguer(Lanche):
    def __init__(self, carne: Carne, queijo, picles, condimento: Condimento):
        super().__init__(carne, condimento)
        self.queijo = queijo
        self.picles = picles

    def preparar(self):
        attCarne = int(input("Hambúrguer de quê?\n1 - Bovíno\n2 - De frango\n"))


        if attCarne == 1:
            self.carne = Vaca()
        elif attCarne == 2:
            self.carne = Frango()
        else:
            print("Por favor Escolher uma opção válida\n")

        attQueijo = int(input("Qual queijo?\n1 - Cheddar\n2 - Mussarela\n"))

        if attQueijo == 1:
            self.queijo = "cheddar"
        elif attCarne == 2:
            self.queijo = "mussarela"
        else:
            print("Por favor escolher uma opção válida\n")

        attPicles = int(input("Picles?\n1 - Sim\n2 - Não\n"))

        if attPicles == 1:
            self.picles = "picles"
        elif attPicles == 2:
            self.picles = "sem picles"
        else:
            print("Por favor escolher uma opção válida\n")

        attCond = int(input("Quais condimentos?\n1 - Ketchup\n2 - Mostarda\n3 - Os dois\n"))

        if attCond == 1:
            self.condimento = Ketchup()
        elif attCond == 2:
            self.condimento = Mostarda()
        elif attCond == 3:
            self.condimento = Both()
        else:
            print("Por favor escolher uma opção válida\n")

        print(f"O seu pedido é: Um hambúrguer {self.carne.grelhar()} com {self.queijo}, {self.picles} e {self.condimento.adicionar()}")

class Salchipao(Lanche):
    def __init__(self, carne: Carne, molho, ovo, condimento: Condimento):
        super().__init__(carne, condimento)
        self.molho = molho
        self.ovo = ovo

    def preparar(self):
        attCarne = int(input("Salsichão de quê?\n1 - Bovíno\n2 - De frango\n"))

        if attCarne == 1:
            self.carne = Vaca()
        elif attCarne == 2:
            self.carne = Frango()
        else:
            print("Por favor Escolher uma opção válida\n")

        attMolho = int(input("Molho?\n1 - Sim\n2 - Não\n"))

        if attMolho == 1:
            self.molho = "com molho"
        elif attMolho == 2:
            self.molho = "sem molho"
        else:
            print("Por favor Escolher uma opção válida\n")

        attOvo = int(input("Ovo?\n1 - Sim\n2 - Nâo\n"))

        if attOvo == 1:
            self.ovo = "com ovo"
        if attOvo == 2:
            self.ovo = "sem ovo"
        else:
            print("Por favor Escolher uma opção válida\n")

        attCond = int(input("Quais condimentos?\n1 - Ketchup\n2 - Mostarda\n3 - Os dois\n"))

        if attCond == 1:
            self.condimento = Ketchup()
        elif attCond == 2:
            self.condimento = Mostarda()
        elif attCond == 3:
            self.condimento = Both()
        else:
            print("Por favor escolher uma opção válida\n")

        print(f"O seu pedido é: Um salchipão {self.carne.grelhar()} {self.molho}, {self.ovo} e {self.condimento.adicionar()}")