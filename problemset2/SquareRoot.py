import math as m

for i in range(1, 10):
    print(i, end='|')
    n_sqrt = m.sqrt(i)
    print(str(n_sqrt).ljust(20 - len(str(n_sqrt))), end='|')
    x = 3.0
    y = (x + i / x) / 2
    print(y)
