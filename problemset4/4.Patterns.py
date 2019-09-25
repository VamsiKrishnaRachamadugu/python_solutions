"""4.Write both a nonrecursive and recursive function that displays the rows of asterisks given below,

"""


def non_recursive(n):
    k = n - 1
    for i in range(0, n):

        for j in range(0, k):
            print(' ', end='')

        k = k - 1

        for j in range(0, i + 1):
            print('*', end='')
        for j in range(0, i):
            print('*', end='')

        print()


def recursive(n, k):
    if k == 0:
        return;
    for i in range(0, k - 1):
        print(' ', end='')
    for i in range(k - 1, n):
        print('*', end='')
    m = n - k
    for i in range(n, n + m):
        print('*', end='')
    print()
    recursive(n, k - 1)


n = 5
recursive(n, n)
non_recursive(n)
