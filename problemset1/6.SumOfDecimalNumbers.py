"""6.Let s be a string that contains a sequence of decimal numbers separated by commas,
e.g., s = '1.23,2.4,3.123'. Write a program that prints the sum of the numbers in s."""
deci_numbers = input('Enter decimal values by using , :')
deci_numbers_list = deci_numbers.split(',')
total = 0
for i in deci_numbers_list:
    total = total + float(i)
print(total)
