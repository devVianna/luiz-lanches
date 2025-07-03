import unittest
from lanche import *
from implementacao import *

class TestCondimentos(unittest.TestCase):
    def test_ketchup_adicionar(self):
        ketchup = Ketchup()
        self.assertEqual(ketchup.adicionar(), "ketchup")

    def test_mostarda_adicionar(self):
        mostarda = Mostarda()
        self.assertEqual(mostarda.adicionar(), "mostarda")

    def test_both_adicionar(self):
        both = Both()
        self.assertEqual(both.adicionar(), "ketchup e mostarda")

class TestCarnes(unittest.TestCase):
    def test_vaca_grelhar(self):
        vaca = Vaca()
        self.assertEqual(vaca.grelhar(), "bovíno")

    def test_frango_grelhar(self):
        frango = Frango()
        self.assertEqual(frango.grelhar(), "de frango")

if __name__ == '__main__':
    unittest.main()