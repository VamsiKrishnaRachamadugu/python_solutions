"""3.Write a program that asks the user to input 10 integers, and then prints the largest odd number that was entered.
If no odd number was entered, it should print a message to that effect."""

li1 = input('Enter 10 numbers with space').split()
maxi = li1[0]
if len(li1) != 0:
    for i in li1:
        if i > maxi and i%2!=0:
            maxi = i
    print('Max ODD value:', maxi)
else:
    print('None of the are odd values')
