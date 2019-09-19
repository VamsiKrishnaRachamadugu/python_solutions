"""list functions """
a=[1,2,3]
b=[4,5,6]
c=a.copy()
c.append('v')
print(a)
print(c)
# a.extend(b)
# a=a+b
# print(a)

"printing even list"
# li=[1,2,3,4,5,6,2,34,2,52,2]
# li = []
# for i in range(1, 10):
#     if i % 2 == 0:
#         li.append(i)
# print(li)

"count of the digits and characters"
count_of_char = 0
count_of_digits = 0
li = [1, 'q', 'w', '1', 1, 's']
# for i in li:
#     if type(i) == int:
#         count_of_digits += 1
#     else:
#         count_of_char += 1
# print(count_of_digits, count_of_char)
# for i in li:
#      if ord(str(i))>=65 and ord(str(i))<=90:
#         count_of_char += 1
#      else:
#         count_of_digits += 1
# print(count_of_digits, count_of_char)

" eliminate duplicates  and printing each character 2 times "
# str1 = input('Enter your string:')
# li1 = []
# for i in str1:
#     if i not in li1:
#         li1.extend(2 * i)
# print(li1)


# li1.remove('a')
# print(li1)

' eliminating only consecutives  and printing each character 2 times '

# str1 = input('Enter your string:')
# li1 = []
# for i in range(len(str1)):
#     if str1[i - 1] != str1[i]:
#         li1.extend(2 * str1[i])
# print(li1)

# name= input('Enter your string:')
# li=[]
# prev=name[0]
# li.append(prev)
# li.append(prev)
# for i in name[1:]:
#     if prev!=i:
#         li.append(i)
#         li.append(i)
#         prev=i
# print(li)


"""print("HEllo""
      "World")"""
'for loops'
# even_sum = 0
# odd_sum = 0
# a, b = int(input('starting value: ')), int(input('ending value: '))
# for i in range(a, b):
#     if i % 2 == 0:
#         even_sum += i
#     else:
#         odd_sum += i
# print('Even  Sum: ', even_sum, ' Odd  Sum: ', odd_sum)
