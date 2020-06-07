from app.getters.InputForFibanacci import getInputDatatoFindFibSeries
from app.loggers.PrintFibanacciSeries import printFibanacciSeries

'''
The method generateFibanacciSeries generate the series of n fibanacci numbers 
'''
def generateFibanacciSeries(number):
    fibanacci_series = []
    previousFibNumber = 1
    currentFibNumber = 1
    for index in range(number):
        fibanacci_series.append(previousFibNumber)
        tempNumber = previousFibNumber
        previousFibNumber = currentFibNumber
        currentFibNumber = currentFibNumber + tempNumber
    return fibanacci_series

'''
main function to get the input data and processing the data and printing the output
'''
def main():
    number = getInputDatatoFindFibSeries() #getting the input
    fibanacci_series = generateFibanacciSeries(number) #generating the n fibanacci numbers
    printFibanacciSeries(fibanacci_series) #printing the fibanacci series

if __name__ == "__main__":
    main() #calling main method