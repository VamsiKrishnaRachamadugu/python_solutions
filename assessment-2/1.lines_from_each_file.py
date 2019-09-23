"""1.Write a Python program to combine each line from first file with the corresponding line in second file"""

file1_text = open('C:\\Users\\A08019dirp_C2e.03.06\\Documents\\test.txt', 'r')
file2_text = open('C:\\Users\\A08019dirp_C2e.03.06\\Desktop\\python_training\\assessment-2.txt', 'r')
data1 = file1_text.readlines()
data2 = file2_text.readlines()
new_file = open('C:\\Users\\A08019dirp_C2e.03.06\\Documents\\new_file.txt', 'w')
result = list(zip(data1, data2))
for line1, line2 in result:
    new_file.write(line1)
    new_file.write(line2)
if len(data1) > len(data2):
    for line in range(len(result), len(data1)):
        new_file.write(data1[line])
else:
    for line in range(len(result), len(data2)):
        new_file.write(data2[line])
file1_text.close()
file2_text.close()
new_file.close()