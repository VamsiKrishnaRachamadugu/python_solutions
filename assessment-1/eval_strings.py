ip_list = ['five plus three', 'seven minus two', 'two plus eight minus five', 'eight divide four']
ref_dict = {'plus': '+', 'minus': '-', 'divide': '/', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'seven': '7',
            'eight': '8'}
p_list = []
for i in ip_list:
    str_list = i.split(' ')
    string = ''
    for j in str_list:
        string = string + ref_dict[j]
    p_list.append(string)
op_list = []
for i in p_list:
    for j, k in ref_dict.items():
        if str(int(eval(i))) == k:
            op_list.append(j)
print(op_list)
