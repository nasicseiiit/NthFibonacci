import unittest

from app.values.FibanacciSeries import generateFibanacciSeries


class FibanacciTest(unittest.TestCase):
    '''
    To test the whether the fibaancci series is generated as expected for all the numbers
    '''
    def testFibanacciSeries(self):
        self.assertEqual(generateFibanacciSeries(1),[1])
        self.assertEqual(generateFibanacciSeries(5), [1,1,2,3,5])
        self.assertEqual(generateFibanacciSeries(0), [])
        self.assertEqual(generateFibanacciSeries(-1), [])
        self.assertEqual(generateFibanacciSeries(7), [1, 1, 2, 3, 5,8,13])

if __name__ == '__main__':
    unittest.main()
