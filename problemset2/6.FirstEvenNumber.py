"""6.Implement a function that satisfies the specification. Use a try-except block.
def findAnEven(l):
	"Assumes l is a list of integers
	Returns the first even number in l
	Raises ValueError if l does not contain an even number"
	"""


def findAnEven(l):
    for i in l:
        if i % 2 == 0:
            return i
    else:
        return ValueError


list1 = [1, 11, 341, 41]
try:
    print(findAnEven(list1))
except ValueError:
    print("Error")
