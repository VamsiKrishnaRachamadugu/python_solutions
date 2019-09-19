def is_palindrome(m_str):
    if m_str[::-1] == m_str:
        return


string = (input('Enter a String to check Palindrome')).lower()
if is_palindrome(string):
    print("Palindrome")
else:
    print("Not a palindrome")
