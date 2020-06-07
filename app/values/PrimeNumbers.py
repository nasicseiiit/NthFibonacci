from app.getters.InputForIsPrime import getInputDatatoFindIsItaPrime
from app.loggers.PrintNumberIsPrime import printisPrimeOrNot

'''
The method isItPrime will check whether the number is prime or not 
'''

def isItPrime(number):
    if(number<=1):
        return "It is not a prime number"
    else:
        for index in range(2, number):
            if (number % index) == 0:
                return "It is not a prime number"
        else:
            return "It is a prime number"


'''
main function to get the input data and processing the data and printing the output
'''
def main():
    number = getInputDatatoFindIsItaPrime() #getting the input
    isPrimeOrNot = isItPrime(number) #finding wether the number is prime or not
    printisPrimeOrNot(isPrimeOrNot) #printing whether the number is prime or not

if __name__ == "__main__":
    main() #calling main method