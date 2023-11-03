import unittest
from Human import Human

class TestMonModule(unittest.TestCase):
    
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.h = Human("remi", 12, 24) 
    
    def test_3(self):
        self.assertEqual(self.h.pv, 24)
    
    def test_2(self):
        self.assertEqual(self.h.nom, "remi")

# python -m unittest Human_test.py