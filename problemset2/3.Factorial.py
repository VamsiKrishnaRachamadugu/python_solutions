"""3.Observe the following function definitions.
They Calculate the Factorial as per the Mathematical definition 1! = 1 (n + 1)! = (n + 1) * n!
Implement factI(n) as an Iterative Implementation & factR(n) as a Recursive Implementation"""


def factI(n):
    fact = 1
    if n == 0:
        return 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def factR(n):
    if n == 0:
        return 1
    else:
        return n * factR(n - 1)


num = 5
print(factI(num))
print(factR(num))
