"""8.Write a function called is_abecedarian that returns True if the letters in a word appear
in alphabetical order (double letters are ok). How many abecedarian words are there? (i.e) "Abhor"
or "Aux" or "Aadil" should return "True" Banana should return "False"
"""


def is_abecedarian(word):
    for i in range(len(word)):
        if i == len(word) - 1 :
            return True
        elif ord(word[i]) <= ord(word[i + 1]):
            continue
        else:
            return False


print(is_abecedarian('vamsi'))
