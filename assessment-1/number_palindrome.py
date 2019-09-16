number = 151
temp = number
r_number = 0
while temp > 0:
    rem = int(temp % 10)
    r_number = int(r_number * 10) + rem
    temp = int(temp / 10)
print(r_number)
