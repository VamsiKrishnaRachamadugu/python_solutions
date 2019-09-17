"""9.Write a function called is_sorted that takes a list as a parameter and returns True 
if the list is sorted in ascending order and False otherwise. You can assume (as a precondition)
 that the elements of the list can be compared with the relational operators <, >, etc. 
 For example, is_sorted([1,2,2]) should return True and is_sorted(['b','a']) should return False.

"""


def is_sorted(li):
    for i in range(len(li)):
        if i == len(li) - 1:
            return True
        elif ord(str(li[i])) <= ord(str(li[i + 1])):
            continue
        else:
            return False


li = [1, 2, 3, 4, 's']
print(is_sorted(li))
