string = 'aabbdddswww'
count = 1
present = string[0]
result_string = ''
for i in range(1, len(string)):
    if present == string[i]:
        count = count + 1
    else:
        if count != 1:
            result_string = result_string + string[i - 1] + str(count)
            present = string[i]
            count = 1
        else:
            present = string[i]
            count = 1
if count != 1:
    result_string = result_string + string[i] + str(count)
print(result_string)
