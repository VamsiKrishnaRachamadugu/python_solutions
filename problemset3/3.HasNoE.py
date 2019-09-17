"""3.In 1939 Ernest Vincent Wright published a 50,000 word novel called Gadsby that does not contain the letter "e."
Since "e" is the most common letter in English, that’s not easy to do. In fact, it is difficult to construct a solitary
thought without using that most common symbol. It is slow going at first, but with caution and hours of training you can
 gradually gain facility. All right, I’ll stop now. Write a function called has_no_e that returns True if the given word
  doesn’t have the letter "e" in it.

"""


def has_no_e(string):
    value = True
    for i in string:
        if i == 'e':
            value = False
    return value


word = input('Enter a word: ')
print(has_no_e(word))
