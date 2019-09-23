""""5.Write a Python function to check whether a string is a pangram or not.
Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"
"""


def is_pangram(pangram_string):
    char_ascii_values = []

    for i in pangram_string:
        char_ascii_values.append(ord(i.upper()))

    for i in range(65, 91):
        if i not in char_ascii_values:
            break
    else:
        return True


if __name__ == '__main__':
    pangram_string = input('Enter a string to check whether it is pangram or not: ')
    if is_pangram(pangram_string):
        print(pangram_string, ' is a pangram')
    else:
        print(pangram_string, ' is not a pangram')
