def star(func):
    def inner(a,b):
        print('before')
        func(a,b)
        print('after')

    print('Here')
    return inner


@star
def print_msg(a, b):
    print(a, b)


print_msg(5, 7)
# star(print_msg(5, 7))
#
# def display(func):
#     print('Heer')
#     func
#
#
# def dummy():
#     print('dummy')
#
#
# display(dummy())
