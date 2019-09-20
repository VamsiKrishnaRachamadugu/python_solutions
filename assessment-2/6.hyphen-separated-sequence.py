"""6.Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow"""

items_string = input('Enter a string of items seperated with - : ')
items_string_list = items_string.split('-')
items_string_values_dict = {}
items_string_values_list = []
for i in items_string_list:
    items_string_values_dict[i] = ord(i[0])
    items_string_values_list.append(ord(i[0]))
items_string_values_list.sort()

resulterd_string = ''
for item in items_string_values_list:
    for key, value in items_string_values_dict.items():
        if item == value:
            resulterd_string = resulterd_string + key +'-'
print('Result: ', resulterd_string.rstrip('-'))
