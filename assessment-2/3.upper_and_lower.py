"""3.Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12"""

case_string = input('Enter a string: ')
upper_count = 0
lower_count = 0
for letter in case_string:
    if letter.isupper():
        upper_count = upper_count + 1
    elif letter.islower():
        lower_count = lower_count + 1

print('No. of Upper case characters : ', upper_count)
print(' No. of Lower case Characters : ', lower_count)
