import unittest
import Project03

class acceptanceTest(unittest.TestCase):
    
    
    def testUS11(self):
        self.assertEqual(Project03.US11("4 JUL 1996", "N/A", "N/A"), False)
        self.assertEqual(Project03.US11("4 JUL 1996", "4 SEP 1962", "N/A"), True)
        self.assertEqual(Project03.US11("4 JUL 1997", "N/A", "4 SEP 1962"), True)
        self.assertEqual(Project03.US11("4 JUL 1996", "5 JUL 1962", "4 JAN 1996"), True)
        self.assertEqual(Project03.US11("4 JUL 1996", "3 JUL 1998", "N/A"), False)
        
        
if __name__ == '__main__':
    unittest.main()
