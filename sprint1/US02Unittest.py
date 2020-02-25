import unittest

from project03 import *

class TestUS02(unittest.TestCase):
    def test1(self):
        self.assertEqual(US02(1973, 1974, 1990, 5,5,5,4,4,4), True)
    
    def test2(self):
        self.assertEqual(US02(1973, 1974, 1970, 5,5,5,4,4,4), False)
        
    def test3(self):
        self.assertEqual(US02(1973, 1974, 1974, 5,5,4,4,4,4), False)
        
    def test4(self):
        self.assertEqual(US02(1973, 1974, 1974, 5,5,5,4,4,3), False)
    
    def test5(self):
        self.assertEqual(US02(1973, 1974, 1974, 5,5,5,4,4,5), True)
    
        
        
if __name__ == '__main__':
    unittest.main()