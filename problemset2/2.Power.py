"""2.A number, a, is a power of b if it is divisible by b and a/b is a power of b.
Write a function called is_power that takes parameters a and b and returns True if a is a power of b.
Note: you will have to think about the base case."""


def is_power(num1, num2):
    quot = num1 / num2
    if quot != num2:
        if num1 % num2 == 0 and quot % num2 == 0:
            return 'true'
        else:
            return 'false'


print(is_power(32, 2))
