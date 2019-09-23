from functools import reduce

#
# li = [-1, -5, -43, 5, 8, 10, 20, 50, 100]
# "map example"
# a = list(map((lambda x: x * 2), li))
# print(a)
#
# "filter example for list by giving condition "
# filter_list = list(filter(lambda x: x > 0, li))
# print(filter_list)
#
# "filter example for removing vowels in string"
# string = "vamsi"
# vowels = 'aeiou'
# filter_string = list(filter(lambda x: x not in vowels, string))
# print(filter_string)
#
# string1 = 'accenture'
# result_string = list(map(lambda x: x + '1', string1))
# print(result_string)
# req_string = ''
# for i in result_string:
#     req_string = req_string + i
# print(req_string)

"reduce example"
# li = '13564'
# reduce_result = reduce(lambda a, b: int(a) * int(b), li)
# print(reduce_result)

# ip_string = '11664331'
# map_list = list(map(lambda x: x * 2, ip_string))
# reduce_result = reduce(lambda a, b: a + b, map_list)
# print(reduce_result)

# map_list = ''.join(map(lambda x: x * 2, ip_string))
# print(map_list)



