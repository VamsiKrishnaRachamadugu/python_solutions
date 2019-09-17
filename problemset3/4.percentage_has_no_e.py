"""4.Modify the above program to print only the words that have no “e” and compute the percentage
 of the words in the list have no “e.”"""


def has_no_e(string):
    list1 = string.split()
    words = len(list1)
    has_e = 0
    for i in list1:
        if 'e' not in i:
            has_e += 1
            print(i)
    percentage = ((words - has_e) / words) * 100
    print(percentage, '%')


word = input('Enter a word: ')
has_no_e(word)
