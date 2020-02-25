'''
Created on Feb 19, 2020

@author: Vincenzo Susi
'''

import unittest
import Project03

class Test(unittest.TestCase):

    def test01(self):
        self.assertFalse(Project03.US03("9 MAY 2000", "10 FEB 1900"))
    def test02(self):
        self.assertTrue(Project03.US03("9 MAY 2000", "10 FEB 2004"))
    def test03(self):
        self.assertTrue(Project03.US03("15 SEP 1972", "10 OCT 2002"))
    def test04(self):
        self.assertFalse(Project03.US03("27 JAN 1990", "26 JAN 1990"))
    def test05(self):
        self.assertTrue(Project03.US03("1 DEC 1975", "1 DEC 1975"))
        
if __name__ == "__main__":
    unittest.main()