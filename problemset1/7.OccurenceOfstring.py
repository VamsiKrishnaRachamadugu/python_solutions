"""7.Write a function isIn() that accepts two strings as arguments and returns True
if either string occurs anywhere in the other, and False otherwise.
Hint: you might want to use the built-in str operation in."""


def isIn(str1, str2):
    if str1 in str2:
        return True
    elif str2 in str1:
        return True
    else:
        return False


str1 = 'Vamsi Krishna'
str2 = 'Vas'
print(isIn(str1, str2))
