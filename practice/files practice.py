import csv
import json
import io
file_directory = 'C:\\Users\\A08019dirp_C2e.03.06\\Documents\\fun.txt'
#
with open(file_directory, 'r') as fh:
    try:
        obj = fh.read()
    except FileNotFoundError as e:
        print(e)

# with open(file_directory, 'a') as fh:
#     fh.seek(10)
#     fh.write('new line added here')
# with open(file_directory, 'r') as fh:
#     fh.seek(10)
#     print(fh.read())

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
#
# fh = open(file_directory, 'a')
# fh.seek(10,1)
# fh.write('hie')
# fh = open(file_directory, 'r')
# csv_list =fh.readlines()
# for i in csv_list:
#     print(i)
# fh.close()

"csv files practice"

with open("C:\\Users\\A08019dirp_C2e.03.06\\Desktop\\practice.csv", 'a') as fh:
    # li1 = {'marks': 78, 'age': 22}
    data1 = csv.reader(fh)
    print(data1)
    # data1.writerow(li1)

"json files practice"
" if we want to read data from string we use loads() method  "
# in_data = '{"name": "vamsi", "age": 22}'
# pri_object=json.loads(in_data)
# print(pri_object)

" if we want to read data from file we use load() method  "
# with open("C:\\Users\\A08019dirp_C2e.03.06\\Desktop\\json_practice.json") as fh:
#     data = json.load(fh)
# print(data)

"You can convert a dictionary to JSON string using json.dumps() method."

# details_dict ='{"details": [{"name": "vamsi", "age": 22}, {"name": "kadimi", "age": 22}]}'
# json_string = json.dumps(details_dict)
# print(json_string)

"To write JSON to a file in Python, we can use json.dump() method."
# details_dict ='{"details": [{"name": "vamsi", "age": 22}, {"name": "kadimi", "age": 22}]}'
# with open("C:\\Users\\A08019dirp_C2e.03.06\\Desktop\\json_practice.json", 'w') as fh:
#     data = json.dump(details_dict, fh)
