"""list to dictionary"""
a = {"one":1}
a["ones"] = a.pop("one")
print(a)


# list1 = ['Five', 5, 'Six', 6, 'Seven', 7, 'Seven', 7.5, 'Seven', 7.9, 'Nine', 9]
# dict1 = {}
# for i in range(0, len(list1), 2):
#     if type(list1[i]) == str:
#         if list1[i] in dict1:
#             if type(dict1[list1[i]]) != list:
#                 li = [dict1[list1[i]], list1[i + 1]]
#                 dict1[list1[i]] = li
#             else:
#                 dict1[list1[i]].append(list1[i + 1])
#         else:
#             dict1[list1[i]] = list1[i + 1]
# print(dict1)

# "from 2 lists to dictionary"
# list1 = ['Five', 'Six', 'Seven', 'Seven', 'Seven', 'Nine']
# list2 = [5, 6, 7, 7.5, 7.9, 9]
# dict1 = {}
# for i in range(len(list1)):
#     if list1[i] not in dict1:
#         dict1[list1[i]] = list2[i]
#     else:
#         if type(dict1[list1[i]]) != list:
#             li = [dict1[list1[i]], list2[i]]
#             dict1[list1[i]] = li
#         else:
#             dict1[list1[i]].append(list2[i])
#
# print(dict1)
