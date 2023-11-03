import unittest
from Human import Human

class TestMonModule(unittest.TestCase):
    
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        #               nom   age  pv
        self.h = Human("remi", 12, 24) 
    
    def test_1(self):
        self.h = Human("remi", 12, 24) 
        self.assertEqual(self.h.pv + 2, 26)

    def test_2(self):
        self.h = Human("remi", 12, 24) 
        self.assertEqual(self.h.nom, "remi")

    def test_3(self):
            self.h = Human("remi", 12, 24) 
            self.assertEqual(self.h.pv, 24)

    def test_4(self):
            self.h = Human("remi", 12, 24) 
            self.assertEqual(self.h.age, 12)

    def test_5(self):
        self.h = Human("remi", 12, 24) 
        self.h.mourrir()
        self.assertEqual(self.h.pv, 0)

# python -m unittest Human_test.py
