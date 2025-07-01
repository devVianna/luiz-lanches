from abc import ABC, abstractmethod

class Condimento(ABC):

    @abstractmethod
    def adicionar(self):
        pass

class Ketchup(Condimento):
    def adicionar(self):
        return "ketchup"

class Mostarda(Condimento):
    def adicionar(self):
        return "mostarda"

class Both(Condimento):
    def adicionar(self):
        return "ketchup e mostarda"

class Carne(ABC):
    
    @abstractmethod
    def grelhar(self):
        pass

class Vaca(Carne):
    def grelhar(self):
        return "bovíno"

class Frango(Carne):
    def grelhar(self):
        return "de frango"

