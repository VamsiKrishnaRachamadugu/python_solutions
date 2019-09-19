import sys


# if (len(sys.argv) == 4):
try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])
    if a > b & a > c:
        print(a)
    elif b > c:
        print(b)
    else:
        print(c)
# else:
#     print('please give 3 variables')
except IndexError as e:
    print(e)
