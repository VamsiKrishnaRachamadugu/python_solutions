def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
        # First Fibonacci number is 0
    else:
        a = 0
        b = 1
        print a
        print b
        count = 2
        for i in range(1, n):
            c = a + b
            count += 1
            a = b
            b = c
            if count == 9:
                print c
                break
            print c


def recur_fibo(n):
    if n <= 1:
        return n
    elif n == 0:
        return 0

    elif n == 1:
        return 1
    else:
        return (recur_fibo(n - 1) + recur_fibo(n - 2))


num = 9
Fibonacci(num)
for i in range(num):
    print recur_fibo(i)
