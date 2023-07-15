'''- Program to read data from a CSV and convert it to a dictionary, then print the details on the 
console. The input content will be in a file, and the employee ID will be the key, while the employee 
details will be the value in the dictionary.
'''

import csv

dicts = {}
with open("students.csv","r") as file1:
    readed = csv.DictReader(file1)
    for i in readed:
        rollno = i["ROLLno"]
        dicts[rollno] = i

try:      
    keyval = input("enter the keyindex")
    print(dicts[keyval])
except Exception as error:
    print("keys is not founded",error)