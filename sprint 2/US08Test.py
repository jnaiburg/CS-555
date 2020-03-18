import unittest
import Project03

class acceptanceTest(unittest.TestCase):
    
    
    def testUS08(self):
        self.assertEqual(Project03.US08("4 JUL 1996", "4 SEP 1962", "4 SEP 2000"), True)
        self.assertEqual(Project03.US08("4 JUL 1996", "4 SEP 1962", "N/A"), True)
        self.assertEqual(Project03.US08("4 JUL 1997", "4 SEP 2000", "N/A"), False)
        self.assertEqual(Project03.US08("4 JUL 1996", "5 JUL 1962", "4 JAN 1996"), True)
        self.assertEqual(Project03.US08("4 JUL 1996", "3 JUL 1962", "4 SEP 1990"), False)
        
        
if __name__ == '__main__':
    unittest.main()
