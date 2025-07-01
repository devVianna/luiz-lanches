from lanche import *
from implementacao import *

ketchup = Ketchup()
mostarda = Mostarda()
both = Both()
vaca = Vaca()
frango = Frango()

hamburguer = Hamburguer(vaca, "cheddar", "picles", ketchup)
salchipao = Salchipao(frango, "barbecue", "ovo", mostarda)

print(hamburguer.preparar())
print(salchipao.preparar())