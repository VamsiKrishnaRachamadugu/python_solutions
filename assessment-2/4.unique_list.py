"""4.Write a Python function that takes a list and returns a new list with unique elements of the first list. Without using set
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
"""
sample_list=input('Enter some elements by adding space').split(' ')
unique_list=[]
for i in sample_list:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)