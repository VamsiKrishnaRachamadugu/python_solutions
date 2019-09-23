import csv
import json

# file_directory = 'C:\\Users\\A08019dirp_C2e.03.06\\Documents\\test.txt'
# """FILE READ OPERATION
#     READS FILE AND IN READLINES() FUNCTION WE NEED TO FOR LOOP AND PRINT EACH LINE """
# fh = open(file_directory, 'r')
# # lis1 = fh.readlines()
# # print(lis1)
# for i in fh:
#     print(i)
"APPENDING AND READING A EXISTING  FILE BY USING 'a'" \
"IF THE FILE DOESN'T EXIST IT WILL CREATE NEW FILE AND WRITE INTO A FILE"
# fh = open(file_directory, 'a')
# fh.write('\nThis line is file operations example ')
# fh.close()
# fh = open(file_directory, 'r')
# print(fh.read())
# fh.close()

# fh = open(file_directory, 'a')
# fh.seek(10,1)
# fh.write('hie')
# fh = open(file_directory, 'r')
# csv_list =fh.readlines()
# for i in csv_list:
#     print(i)
# fh.close()

"csv files practice"

# with open("C:\\Users\\A08019dirp_C2e.03.06\\Desktop\\practice.csv", 'a') as fh:
#     li1 = {'marks': 78, 'age': 22}
#     data1 = csv.writer(fh)
#     data1.writerow(li1)

"json files practice"
# in_data = {
#     'details':
#         [
#
#             {
#                 'name': 'vamsi',
#                 'age': 22
#             },
#             {
#                 'name': 'kadimi',
#                 'age': 22
#             }
#         ]
# }
in_data = {'name': 'vamsi', 'age': 22}
with open("C:\\Users\\A08019dirp_C2e.03.06\\Desktop\\json_practice.json") as fh:
    data = json.dump(in_data, fh)
