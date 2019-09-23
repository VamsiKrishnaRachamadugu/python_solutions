"""7.Write a function named using_only() that takes a word and a string of letters, and that returns True
if the word contains only letters in the list. Can you make a sentence using only the letters acefhlo?
Other than "Hoe alfalfa?"

"""


def using_only(word, letters_string):
    for char in word:
        if char not in letters_string:
            return False
    else:
        return True


in_word = input('Enter the name: ')
letter_string = input('Enter charceters: ')
print(using_only(in_word, letter_string))
