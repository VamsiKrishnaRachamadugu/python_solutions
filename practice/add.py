import sys

print(sys.argv[1])
a = int(sys.argv[1])
b = 0

li = list(sys.argv[2])
for i in li:
    if i.isdigit():
        b = b + int(i)
print(a, b)
