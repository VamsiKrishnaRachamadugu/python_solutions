"""2.Count new lines in file"""

file1_text = open('C:\\Users\\A08019dirp_C2e.03.06\\Documents\\test.txt', 'r')
file_read = file1_text.readlines()
length = len(file_read)
print('New lines', length)
file1_text.close()
