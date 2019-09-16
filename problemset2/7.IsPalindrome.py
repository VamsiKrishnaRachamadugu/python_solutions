"""7.A palindrome is a word that is spelled the same backward and forward, l
ike "Malayalam" and "Noon" . Recursively, a word is a palindrome if the first and last letters are
the same and the middle is a palindrome. Write a function called is_palindrome that takes a string
argument and returns True if it is a palindrome and False otherwise. Remember that you can use the
built-in function len to check the length of a string.
Use the function definition"""


def is_palindrome(m_str):
    reverse_string = ''
    # reverse_string = "".join(reversed(m_str))

    for i in m_str:
        reverse_string = i +reverse_string
    return reverse_string == m_str


string = (input('Enter a String to check Palindrome')).lower()
if is_palindrome(string):
    print("Palindrome")
else:
    print("Not a palindrome")
