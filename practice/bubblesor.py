def bubblesort(li):
    for i in range(len(li)):
        for j in range(0, len(li) - i - 1):
            if li[j] > li[j + 1]:
                temp = li[j]
                li[j] = li[j + 1]
                li[j + 1] = temp
    # return li


b_list = [2, 31, 3, 1, 54, 1, 3, 1, 5, 2]
bubblesort(b_list)
print(b_list)
