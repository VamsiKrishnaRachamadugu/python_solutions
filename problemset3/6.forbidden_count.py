"""6.Modify your program to prompt the user to enter a string of forbidden letters and
then print the number of words that don’t contain any of them. Can you find a combination
of 5 forbidden letters that excludes the smallest number of words?"""


def avoids(word, string):
    count = 0
    for char in word:
        if char not in string:
            count = count + 1
    return count


words = input('Enter the sentence: ')
forbidden_letters = input('Enter forbidden letters')
print(avoids(words, forbidden_letters))
