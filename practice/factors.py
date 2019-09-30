def factors(n):
    for i in range(1, n):
        if n % i == 0:
            print i
    print n


factors(24)
