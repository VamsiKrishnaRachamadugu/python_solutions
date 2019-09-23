"""1.A string slice can take a third index that specifies the "step size;" that is, the number of spaces between
successive characters. A step size of 2 means every other character; 3 means every third, etc.
fruit = 'banana'
 fruit[0:5:2]
'bnn'"""


def is_palindrome(in_string):
    if in_string == in_string[::-1]:
        return True
    else:
        return False


in_string = input('Enter a string to validate for palindrome: ')
print(is_palindrome(in_string))
