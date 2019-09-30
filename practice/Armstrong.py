def isArmstrong(num):
    n = digits(num)
    result = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        result = result + digit ** n
        temp /= 10
    return result


def digits(n):
    count = 0
    while n != 0:
        count += 1
        n /= 10
    return count


num = input('Enter the number')

if isArmstrong(num) == num:
    print num, ' is armstrong number'
else:
    print num, ' is not an armstrong number'
