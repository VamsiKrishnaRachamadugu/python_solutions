"""1.Write a program that examines three variables—x, y, and z— and prints
the largest odd number among them. If none of them are odd, it should print a message to that effect."""
a, b, c = 2, 4, 6
odd_list = []
if a % 2 != 0:
    odd_list.append(a)
elif b % 2 != 0:
    odd_list.append(b)
elif c % 2 != 0:
    odd_list.append(c)
if len(odd_list)!=0:
    maxi = odd_list[0]
    for i in odd_list:
        if i > maxi:
            maxi = i
    print('Max ODD value:', maxi)
else:
    print('None of the are odd values')



