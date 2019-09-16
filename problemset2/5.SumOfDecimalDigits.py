"""5.Implement a function that meets the specification below. Use a try-except block.

def sumDigits(s):
	Assumes s is a string
	Returns the sum of the decimal digits in s
	For example, if s is 'a2b3c' it returns 5"""

string = input('Enter the list of numbers')


def sumDigits(s):
    list2 = []
    sum = 0
    for i in string:
        if i.isdigit():
            list2.append(i)
            sum += int(i)
    print(sum)


try:
    sumDigits(string)
except:
    print('Error')
