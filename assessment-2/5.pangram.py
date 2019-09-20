def is_pangram(pangram_string):
    char_ascii_values = []

    for i in pangram_string:
        char_ascii_values.append(ord(i.upper()))

    for i in range(65, 91):
        if i not in char_ascii_values:
            break
    else:
        return True


pangram_string = input('Enter a string to check whether it is pangram or not: ')
if is_pangram(pangram_string ):
    print(pangram_string, ' is a pangram')
else:
    print(pangram_string, ' is not a pangram')

