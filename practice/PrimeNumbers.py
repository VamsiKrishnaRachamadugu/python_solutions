def prime(num1, num2):
    if num1 > num2:
        print('invalid values')
    else:
        while num1 != num2:
            isPrime(num1)
            num1 += 1


def isPrime(num):
    count = 2

    for i in range(count, num + 1):
        if num % count == 0:
            break
        else:
            print(num)


num11 = input("Enter the 1st number: ")
num21 = input("Enter the 2nd number: ")
prime(num11, num21)
