"""8.The built-in function eval takes a string and evaluates it using the Python interpreter. For example:
 eval('1 + 2 * 3')
7
import math
eval('math.sqrt(5)')
2.2360679774997898
eval('type(math.pi)')
<type 'float'>"""


def eval_loop():
    li = []
    result = 'false'
    while result == 'false':
        string = input('Enter expression')
        if string == 'done':
            print(li)
            result = 'true'
            break
        else:
            li.append(eval(string))
            continue


eval_loop()
