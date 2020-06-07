import unittest

from app.values.PrimeNumbers import isItPrime


class PrimeTest(unittest.TestCase):
    '''
    test to check is even numbers or prime or not
    '''
    def testIsEvenNumbersPrime(self):
        self.assertEqual(isItPrime(2), "It is a prime number")
        self.assertEqual(isItPrime(8), "It is not a prime number")
        self.assertEqual(isItPrime(16), "It is not a prime number")

    '''
        test to check is odd numbers or prime or not
    '''
    def testIsOddNumbersPrime(self):
        self.assertEqual(isItPrime(5), "It is a prime number")
        self.assertEqual(isItPrime(2), "It is a prime number")
        self.assertEqual(isItPrime(9), "It is not a prime number")
        self.assertEqual(isItPrime(1), "It is not a prime number")

    '''
        test to check is negative numbers or prime or not
    '''
    def testIsNegativeNumbersPrime(self):
        self.assertEqual(isItPrime(-5), "It is not a prime number")
        self.assertEqual(isItPrime(-10), "It is not a prime number")


if __name__ == '__main__':
    unittest.main()
