"""2.Write a function called rotate_word() that takes a string and an integer as parameters,
and that returns a new string that contains the letters from the original string "rotated" by
the given amount. For example, "cheer" rotated by 7 is "jolly" and "melon" rotated by -10 is "cubed".
You might want to use the built-in functions ord, which converts a character to a numeric code, and chr,
which converts numeric codes to characters.

"""


def rotate_word(string, number):
    final_string = ''
    for i in string:
        num = ord(i)
        trans_string = num + number
        final_string += chr(trans_string)
    return final_string


name = input('Enter a string: ')
num = int(input('Enter a number: '))
print(rotate_word(name, num))
