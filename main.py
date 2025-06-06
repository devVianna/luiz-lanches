from lanche import *
from implementacao import *

ketchup = Ketchup()
mostarda = Mostarda()
both = Both()
boi = Boi()
frango = Frango()

hamburguer = Hamburguer(boi, "cheddar", "picles", ketchup)
salsipao = (Frango, "barbecue", "ovo", mostarda)

print(hamburguer.preparar())
print(salsipao.preparar())