import unittest
import cps2411function

class productTest(unittest.TestCase):

    def testProduct(self):
        ans = cps2411function.cps2411(7)
        self.assertEqual(422, ans)
        

if __name__ == '__main__':
    unittest.main()
