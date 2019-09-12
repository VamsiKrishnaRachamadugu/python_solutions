"""3.Write a program that asks the user to input 10 integers, and then prints the largest odd number that was entered.
If no odd number was entered, it should print a message to that effect."""

li1 = input('Enter 10 numbers with space').split()
odd_list = []
if len(li1)==0:
    print('Enter some values')
else:
    for i in li1:
        if int(i) % 2 != 0:
            odd_list.append(int(i))
    maxi = odd_list[0]
    if len(odd_list) != 0:
        for i in odd_list:
            if i > maxi:
                maxi = i
        print('Max ODD value:', maxi)
    else:
        print('None of the are odd values')
