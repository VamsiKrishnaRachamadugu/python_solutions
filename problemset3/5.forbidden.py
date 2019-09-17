"""5.Write a function named avoids that takes a word and a string of forbidden letters, and
that returns True if the word doesn’t use any of the forbidden letters.

"""


def avoids(word, string):
    value = True
    for i in string.lower():
        if i in word:
            value = False
            break
        else:
            continue
    return value


words = input('Enter the sentence: ')
forbidden_letters = input('Enter forbidden letters')
print(avoids(words, forbidden_letters))
