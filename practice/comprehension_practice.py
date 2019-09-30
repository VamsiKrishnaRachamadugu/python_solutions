# li = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
# result = ''.join([j for i in li for j in i])
# print(result)
# li=[2000,20001,20003]
# result={i:('yes'if i%100==0 & i%4==0 else 'no') for i in li }
#
# n = 10
# result = [i for i in range(1, n + 1) if all(i % j != 0 for j in range(2, i))]
# print(result)

list1 = [i for i in range(1, 10) for j in range(2, i) if i % j == 0 and i != j]
result = [i for i in range(1, 10) if i not in list1]
print(result)
