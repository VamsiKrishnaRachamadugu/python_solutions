class StringArgumentException(Exception):
    pass


i = int(input('Enter a value: '))
try:
    if type(i) != str:
        raise StringArgumentException('wrong entry')
        # raise ValueError
except Exception as e:
    print('wrong entry')
except StringArgumentException as se:
    print('string entry')
except ValueError as ve:
    print('value error')
