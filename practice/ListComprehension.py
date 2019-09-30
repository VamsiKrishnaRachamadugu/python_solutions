# even numbers
inputList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 342, 4, 24, 2]
outputList = [var for var in inputList if var % 2 == 0]
print outputList

# squares of 1-10 numbers

squareNumberList = [var ** 2 for var in range(1, 10)]
print squareNumberList