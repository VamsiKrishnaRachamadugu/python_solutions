def isPrime(num):
    count = 2

    k = 0
    for i in range(count, num + 1):
        if num % count == 0:
            return False
            k += 1
        else:
            continue
    if k == 0:
        return True


print  isPrime(6)
