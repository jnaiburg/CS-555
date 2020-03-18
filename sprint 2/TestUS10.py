import unittest
import US10 as Project03

class acceptanceTest(unittest.TestCase):
    
    
    def testUS10(self):
        self.assertEqual(Project03.US10("4 JUL 1000", "4 JUL 999"), False)
        self.assertEqual(Project03.US10("4 JUL 2040", "4 AUG 2020"), True)
        self.assertEqual(Project03.US10("4 JUL 2038", "4 SEP 2018"), True)
        self.assertEqual(Project03.US10("4 JUL 2011", "4 JUL 2010"), False)
        self.assertEqual(Project03.US10("4 JUL 2060", "4 JUL 2030"), True)
        
        
if __name__ == '__main__':
    unittest.main()
