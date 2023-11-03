import unittest
from Human import Human

class TestMonModule(unittest.TestCase):
    
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.h = Human("remi", 12, 15) 

    def test_1(self):
        self.assertEqual(self.h.pv, 15)
    
    def test_2(self):
        self.assertEqual(self.h.nom, "remi")

# python -m unittest test