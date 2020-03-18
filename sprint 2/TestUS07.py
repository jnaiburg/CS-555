import unittest
import US07 as Project03

class acceptanceTest(unittest.TestCase):
    
    
    def testUS07(self):
        self.assertEqual(Project03.US07("4 JUL 1000"), False)
        self.assertEqual(Project03.US07("4 JUL 1996"), True)
        self.assertEqual(Project03.US07("4 JUL 1997"), True)
        self.assertEqual(Project03.US07("4 JUL 1996"), True)
        self.assertEqual(Project03.US07("4 JUL 1996"), True)
        
        
if __name__ == '__main__':
    unittest.main()
