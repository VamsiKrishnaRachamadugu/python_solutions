def count_of_characters(str):
    dicto = {}
    for i in str:
        if i not in dicto:
            dicto[i] = 1
        else:
            dicto[i] += 1
    print dicto


count_of_characters('aaaaabbbyyykkk')
