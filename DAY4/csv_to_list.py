'''- Read a CSV file that has employee details, convert it to an Object (have a class for an employee), 
and keep the object in a list.'''

import csv
class students:
    def __init__(self,Rollno,name,avg,mark):
        self.rollno = Rollno
        self.name = name
        self.avg = avg
        self.mark = mark

list1 = []
with open("students.csv","r") as file1:
    data = csv.DictReader(file1)
    for i in data:
        obj=students(i["ROLLno"],i["NAME"],i["AVG"],i["MARK"])
        list1.append(obj)

for i in list1:
  print(i.rollno,i.name,i.avg,i.mark)
