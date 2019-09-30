inputNumber = 1011
decimal = 0
power = 0
while inputNumber != 0:
    rem = inputNumber % 10
    decimal += rem * 2 ** power
    inputNumber /= 10
    power += 1
print decimal
