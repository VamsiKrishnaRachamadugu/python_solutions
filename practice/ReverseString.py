name = raw_input('Enter your name')


# calling function
def reverse_string(string):
    reverse_str = ''
    length=len(string) - 1
    while length>=0:
        reverse_str =reverse_str+ string[length]
        length=length-1
    print reverse_str


# iteration
reverseName = ''
for i in name:
    reverseName = i + reverseName
print reverseName

# slicing
print name[::-1]

reverse_string(name)