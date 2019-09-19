def star(func):
    def inner(*args,**kwargs):
        func(*args,**kwargs)
    return inner

@star
def print_msg(a,b):
    print(a,b)

print_msg(5,7)