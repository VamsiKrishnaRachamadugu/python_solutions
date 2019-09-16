"""5.Write a program that computes the decimal equivalent of the binary number 10011?"""
inputNumber = 10011
decimal = 0
power = 0
while int(inputNumber) != 0:
    rem = inputNumber % 10
    decimal = int(decimal) + int(rem) * 2 ** power
    inputNumber = inputNumber / 10
    power += 1
print(decimal)
