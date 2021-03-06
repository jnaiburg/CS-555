'''
Created on Feb 19, 2020

@author: Vincenzo Susi
'''

import unittest
import Project03

class Test(unittest.TestCase):

    def test_US03(self):
        self.assertFalse(Project03.US03("9 MAY 2000", "10 FEB 1900"))
        self.assertTrue(Project03.US03("9 MAY 2000", "10 FEB 2004"))
        self.assertTrue(Project03.US03("15 SEP 1972", "10 OCT 2002"))
        self.assertFalse(Project03.US03("27 JAN 1990", "26 JAN 1990"))
        self.assertTrue(Project03.US03("1 DEC 1975", "1 DEC 1975"))
    
    def test_US06(self):
        self.assertFalse(Project03.US06("9 MAY 2000", "10 FEB 1900", "24 MAR 1905"))
        self.assertTrue(Project03.US06("9 MAY 2000", "10 FEB 2004", "24 MAR 2005"))
        self.assertTrue(Project03.US06("15 SEP 1972", "10 OCT 2002", "30 AUG 1980"))
        self.assertFalse(Project03.US06("27 JAN 1990", "26 JAN 1990", "22 JAN 1990"))
        self.assertTrue(Project03.US06("1 DEC 1975", "1 DEC 1975", "1 DEC 1975"))
        
if __name__ == "__main__":
    unittest.main()
