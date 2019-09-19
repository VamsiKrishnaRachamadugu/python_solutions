def gen_practice(list1):
    for i in list1:
        yield i


li = [1, 2, 3, 1, 2, 3, 12, 1, 34]
for i in gen_practice(li):
    print(i)
