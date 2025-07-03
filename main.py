from lanche import *

def start():
    a = int(input("Bem vindo ao Luiz Lanches! O que você gostaria de pedir?\n1 - Hambúrguer\n2 - Salchipão\n"))
    
    if a == 1:
        escolha = Hamburguer(1,1,1,1)
        escolha.preparar()
    elif a == 2:
        escolha = Salchipao(1,1,1,1)
        escolha.preparar()
    else:
        print("Por favor fazer uma escolha válida")
        start()

start()