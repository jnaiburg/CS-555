'''
Created on Feb 19, 2020
@author: Joseph Naiburg, Timothy Leonard, Vincenzo Susi
'''

import unittest
import Project

class acceptanceTest(unittest.TestCase):
    
    def test_US01(self):
        self.assertTrue(Project.US01("9 MAY 2000"))
        self.assertTrue(Project.US01("12 DEC 1977"))
        self.assertFalse(Project.US01("31 OCT 2025"))
        self.assertFalse(Project.US01("1 JAN 2050"))
        self.assertTrue(Project.US01("3 MAR 2000"))
    
    def test_US02(self):
        self.assertEqual(Project.US02("4 JUL 1996", "4 SEP 1962", "4 SEP 1962"), True)
        self.assertEqual(Project.US02("4 JUL 1996", "4 SEP 2000", "4 SEP 1962"), False)
        self.assertEqual(Project.US02("4 JUL 1996", "4 SEP 1996", "4 SEP 1962"), False)
        self.assertEqual(Project.US02("4 JUL 1996", "5 JUL 1996", "4 SEP 1962"), False)
        self.assertEqual(Project.US02("4 JUL 1996", "3 JUL 1996", "4 SEP 1962"), True)
    
    def test_US03(self):
        self.assertFalse(Project.US03("9 MAY 2000", "10 FEB 1900"))
        self.assertTrue(Project.US03("9 MAY 2000", "10 FEB 2004"))
        self.assertTrue(Project.US03("15 SEP 1972", "10 OCT 2002"))
        self.assertFalse(Project.US03("27 JAN 1990", "26 JAN 1990"))
        self.assertTrue(Project.US03("1 DEC 1975", "1 DEC 1975"))
    
    def test_US04(self):
        self.assertFalse(Project.US04("9 MAY 2000", "10 FEB 1900"))
        self.assertTrue(Project.US04("9 MAY 2000", "10 FEB 2004"))
        self.assertTrue(Project.US04("15 SEP 1972", "10 OCT 2002"))
        self.assertFalse(Project.US04("27 JAN 1990", "26 JAN 1990"))
        self.assertTrue(Project.US04("1 DEC 1975", "1 DEC 1976"))
        
    def test_US05(self):
        self.assertEqual(Project.US05("4 JUL 1996", "3 JUL 2001", "N/A"), True)
        self.assertEqual(Project.US05("4 JUL 1996", "N/A", "N/A"), True)
        self.assertEqual(Project.US05("4 JUL 1996", "3 JUL 2001", "3 JUL 1967"), False)
        self.assertEqual(Project.US05("4 JUL 1996", "3 JUL 1996", "N/A"), False)
        self.assertEqual(Project.US05("4 JUL 1996", "3 JUL 2001", "3 APR 2005"), True)
    
    def test_US06(self):
        self.assertFalse(Project.US06("9 MAY 2000", "10 FEB 1900", "24 MAR 1905"))
        self.assertTrue(Project.US06("9 MAY 2000", "10 FEB 2004", "24 MAR 2005"))
        self.assertTrue(Project.US06("15 SEP 1972", "10 OCT 2002", "30 AUG 1980"))
        self.assertFalse(Project.US06("27 JAN 1990", "26 JAN 1990", "22 JAN 1990"))
        self.assertTrue(Project.US06("1 DEC 1975", "1 DEC 1975", "1 DEC 1975"))

    def testUS07(self):
        self.assertEqual(Project.US07("4 JUL 1000"), False)
        self.assertEqual(Project.US07("4 JUL 1996"), True)
        self.assertEqual(Project.US07("4 JUL 1997"), True)
        self.assertEqual(Project.US07("4 JUL 1996"), True)
        self.assertEqual(Project.US07("4 JUL 1996"), True)
        
    def testUS08(self):
        self.assertEqual(Project.US08("4 JUL 1996", "4 SEP 1962", "4 SEP 2000"), True)
        self.assertEqual(Project.US08("4 JUL 1996", "4 SEP 1962", "N/A"), True)
        self.assertEqual(Project.US08("4 JUL 1997", "4 SEP 2000", "N/A"), False)
        self.assertEqual(Project.US08("4 JUL 1996", "5 JUL 1962", "4 JAN 1996"), True)
        self.assertEqual(Project.US08("4 JUL 1996", "3 JUL 1962", "4 SEP 1990"), False)
        
    def test_US09(self):
        self.assertTrue(Project.US09("9 MAY 1910", "10 FEB 1900", "24 MAR 1900"))
        self.assertFalse(Project.US09("9 MAY 1960", "10 FEB 1970", "24 MAR 2005"))
        self.assertTrue(Project.US09("15 SEP 1972", "10 OCT 1971", "20 FEB 1972 "))
        self.assertFalse(Project.US09("27 JAN 1990", "26 JAN 1980", "22 JAN 1985"))
        self.assertTrue(Project.US09("1 DEC 1975", "1 DEC 1975", "1 DEC 1975"))

    def testUS10(self):
        self.assertEqual(Project.US10("4 JUL 1000", "4 JUL 999"), False)
        self.assertEqual(Project.US10("4 JUL 2040", "4 AUG 2020"), True)
        self.assertEqual(Project.US10("4 JUL 2038", "4 SEP 2018"), True)
        self.assertEqual(Project.US10("4 JUL 2011", "4 JUL 2010"), False)
        self.assertEqual(Project.US10("4 JUL 2060", "4 JUL 2030"), True)

    def testUS11(self):
        self.assertEqual(Project.US11("4 JUL 1996", "N/A", "N/A"), False)
        self.assertEqual(Project.US11("4 JUL 1996", "4 SEP 1962", "N/A"), True)
        self.assertEqual(Project.US11("4 JUL 1997", "N/A", "4 SEP 1962"), True)
        self.assertEqual(Project.US11("4 JUL 1996", "5 JUL 1962", "4 JAN 1996"), True)
        self.assertEqual(Project.US11("4 JUL 1996", "3 JUL 1998", "N/A"), False)
        
    def test_US12(self):
        self.assertTrue(Project.US12(30, 30, 30))
        self.assertFalse(Project.US12(80, 50, 15))
        self.assertFalse(Project.US12(40, 100, 12))
        self.assertTrue(Project.US12(45, 45, 20))
        self.assertTrue(Project.US12(50, 60, 15))
        
    def testUS14(self):
        self.assertEqual(Project.US14(["4 JUL 1996", "4 JUL 1996", "4 JUL 1996", "4 JUL 1996", "4 JUL 1996"]), True)
        self.assertEqual(Project.US14(["4 JUL 1996", "4 JUL 1996", "4 JUL 1996", "4 JUL 1996", "3 MAR 1995"]), True)
        self.assertEqual(Project.US14(["4 JUL 1996"]), True)
        self.assertEqual(Project.US14(["4 JUL 1996", "4 JUL 1996", "4 JUL 1996", "4 JUL 1996", "4 JUL 1996", "4 May 1996"]), True)
        self.assertEqual(Project.US14(["4 JUL 1996", "4 JUL 1996", "4 JUL 1996", "4 JUL 1996", "4 JUL 1996", "4 JUL 1996"]), False)

    def test_US15(self):
        self.assertTrue(Project.US15(['@I10@', '@I11@']))
        self.assertFalse(Project.US15(['@I10@', '@I11@', '@I1@', '@I2@', '@I3@', '@I4@', '@I5@', '@I6@', '@I7@',
                                       '@I8@', '@I9@', '@I12@', '@I13@', '@I14@', '@I15@']))
        self.assertTrue(Project.US15('N/A'))
        self.assertFalse(Project.US15(['@I10@', '@I11@', '@I1@', '@I2@', '@I3@', '@I4@', '@I5@', '@I6@', '@I7@',
                                       '@I8@', '@I9@', '@I12@', '@I13@', '@I14@', '@I15@', '@I16@']))
        self.assertTrue(Project.US15([]))
        
    def testUS17(self):
        self.assertEqual(Project.US17("@I1@", "@I2@", []), True)
        self.assertEqual(Project.US17("@I1@", "@I2@", ["@I1@"]), False)
        self.assertEqual(Project.US17("@I1@", "@I2@", ["@I2@"]), False)
        self.assertEqual(Project.US17("@I1@", "@I2@", ["@I3@", "@I4@"]), True)
        self.assertEqual(Project.US17("@I1@", "@I2@", ["@I3@", "@I4@", "@I2@"]), False)

    def test_US18(self):
        self.assertTrue(Project.US15(['@I10@', '@I11@']))
        self.assertTrue(Project.US15([]))
        self.assertTrue(Project.US15('N/A'))
        self.assertTrue(Project.US15(['@I9']))

if __name__ == '__main__':
    unittest.main()
