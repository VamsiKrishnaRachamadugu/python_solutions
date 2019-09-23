"""2.Write a function called rotate_word() that takes a string and an integer as parameters,
and that returns a new string that contains the letters from the original string "rotated" by
the given amount. For example, "cheer" rotated by 7 is "jolly" and "melon" rotated by -10 is "cubed".
You might want to use the built-in functions ord, which converts a character to a numeric code, and chr,
which converts numeric codes to characters.

"""


def rotate_word(string, number):
    final_string = ''

    for i in string:
        ascii_num = ord(i)
        trans_string = ascii_num + number
        if trans_string < 97:
            already_sub = ascii_num - 97
            num1 = number + already_sub
            final_num = 123 + num1
            final_string += chr(final_num)
        elif trans_string > 122:
            already_sub = 122 - ascii_num
            num1 = number - already_sub
            final_num = 96 + num1
            final_string += chr(final_num)
        else:
            final_string += chr(trans_string)
    return final_string


name = input('Enter a string: ')
num = int(input('Enter a number: '))
print(rotate_word(name, num))
