from app.getters.InputForFibanacci import getInputDatatoFindFibSeries
from app.loggers.PrintFibanacciSeries import printFibanacciSeries

'''This is a recursive method to find the fibanacci of iTh term'''
def fibanacci(index):
    if index<=1:
        return index
    return fibanacci(index-1)+fibanacci(index-2)

'''
The method generateFibanacciSeries generate the series of n fibanacci numbers 
'''
def generateFibanacciSeries(number):
    fibanacci_series = []
    for index in range(number):
        iThTerm  = fibanacci(index)
        fibanacci_series.append(iThTerm)
    return fibanacci_series

'''
main function to get the input data and processing the data and printing the output
'''
def main():
    number = getInputDatatoFindFibSeries() #getting the input
    fibanacci_series = generateFibanacciSeries(number+1) #generating the n fibanacci numbers
    printFibanacciSeries(fibanacci_series[1:]) #printing the fibanacci series

if __name__ == "__main__":
    main() #calling main method