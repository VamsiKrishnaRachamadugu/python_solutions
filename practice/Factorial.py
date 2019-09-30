class Fact:
    def non_recursive(self, n):
        fact = 1
        if n == 0:
            return 1
        for i in range(1, n + 1):
            fact *= i
        return fact

    def recursive(self, n):
        if n == 0:
            return 1
        else:
            return n * self.recursive(n - 1)


f = Fact()
num = 5
print f.non_recursive(num)
print  f.recursive(num)
