def isPrime(num):
    count = 2
    k = 0
    for i in range(count, num + 1):
        if num % count == 0:
            k += 1
            factors(num)
            break
        else:
            continue
    if k == 0:
        print 'number is prime'


def factors(n):
    for i in range(1, n):
        if n % i == 0:
            print i
    print n


isPrime(20)
