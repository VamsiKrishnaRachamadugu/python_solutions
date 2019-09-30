def greatestCommon(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return greatestCommon(b, a % b)


def least_common_factor(x, y):
    return (x * y) / greatestCommon(x, y)


num1 = input('Enter 1st value')
num2 = input('Enter 2nd value')
print greatestCommon(num1, num2)
print least_common_factor(num1,num2)
