string = input('Enter a string')
result_dic = {}
for i in string:
    if i in result_dic:
        result_dic[i] = result_dic[i] + 1
    else:
        result_dic[i] = 1
print(result_dic)
result_string = ''
for i in string:
    result_string = result_string + i + str(result_dic[i])
print(result_string)

result_string = ''
for i in result_dic:
    for j in range(result_dic[i]):
        result_string = result_string + i + str(result_dic[i])
print(result_string)
