x = 12


def fun():
    global x
    x = 2
    x = x + 2
    print(str1)


str1 = ''
fun()
