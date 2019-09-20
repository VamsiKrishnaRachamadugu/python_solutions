"""1.Write a Python program to combine each line from first file with the corresponding line in second file"""

file1_text = open('C:\\Users\\A08019dirp_C2e.03.06\\Documents\\test.txt', 'r')
file2_text = open('C:\\Users\\A08019dirp_C2e.03.06\\Documents\\test.txt', 'r')
data1 = file1_text.readlines()
data2 = file2_text.readlines()
new_file = open('C:\\Users\\A08019dirp_C2e.03.06\\Documents\\new_file.txt', 'w')
if len(data1) > len(data2):
    for line in range(len(data1)):
        new_file.write(data1[line])
        new_file.write(data2[line])
else:
    for line in range(len(data2)):
        new_file.write(data1[line])
        new_file.write(data2[line])
