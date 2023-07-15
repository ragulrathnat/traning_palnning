

'''- Program to read all the files in a folder and append the contents in a single file. The program needs 
to accept the input path and output path as parameters.
'''

import os

path = input("enter the path of folder") 

list_of_files = os.listdir(path)
filename = input("enter the filename to append")
fh1 = open(filename,'a')

for file_name in list_of_files:
    if file_name.endswith(".txt"):
        try:
            fh = open(file_name,'r')
            fh1.write(fh.read())
            fh.close()
        except Exception as error:
            print(error)
else:
    print(filename+"is successully appended")

fh1.close()
