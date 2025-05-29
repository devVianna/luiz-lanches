#teste para confirmar numero correto de pães

import unittest
from lanche import Lanche

class TestLanche(unittest.TestCase):
    def test_condimento(self):
        lanche = Lanche("Ketchup")
        condimentos_certos = {"Ketchup", "Mostarda", "Os dois"}
        self.assertIn(lanche.condimento, condimentos_certos)

if __name__ == '__main__':
    unittest.main()