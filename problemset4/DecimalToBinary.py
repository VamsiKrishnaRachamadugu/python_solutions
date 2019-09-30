# number = 34
# binary = ''
# while number != 0:
#     binary = str(int(number % 2))+binary
#     number = int(number) / 2
# print(binary)

# convert to single list
a = [1, [2, 3], [4, 5, [6, 7, [8, [9]]]]]


def convert_to_list(list_elem):
    if type(list_elem) is not type([]):
        return_list.append(list_elem)
    else:
        for elem in list_elem:
            if type(list_elem) is not type([]):
                return_list.append(elem)
            else:
                convert_to_list(elem)


return_list = []
for i in a:
    convert_to_list(i)
print(return_list)
