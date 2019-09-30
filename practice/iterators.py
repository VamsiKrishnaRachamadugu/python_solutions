li = [1, 2, 3, 12, 11]
a = iter(li)
while True:
    try:
        print(a.__next__())
    except StopIteration:
        break
