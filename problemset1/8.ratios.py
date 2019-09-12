"""8.Implement a function that satisfies the specification. Use a try-except block.

def getRatios(vect1, vect2):
	''Assumes: vect1 and vect2 are lists of equal length of numbers
	Returns: a list containing the meaningful values of
	vect1[i]/vect2[i]''
	"""


def getRatios(vect1, vect2):
    return_list = []
    for i in range(len(vect1)):
        ratio = vect1[i] / vect2[i]
        return_list.append(ratio)
    return return_list


list1 = [1, 2, 4, 1, 1, 232, 1]
list2 = [3, 42, 3, 1, 3, 4, 8]
print(getRatios(list1, list2))
