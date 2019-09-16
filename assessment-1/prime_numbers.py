def is_prime(a, b):
    prime_list = []
    if a > b:
        print(a, 'should be less than', b)
    else:
        for i in range(a, b):
            for j in range(2, int(i / 2)):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
        print(prime_list)


is_prime(10, 20)
