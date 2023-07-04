import csv
import json

filename = input("enter the filename")
with open(filename,'w',newline='') as fh:
    w = csv.writer(fh)
    w.writerow(['NAME','ROLLno','MARK','AVG'])

    while True:
        name = input("enter the name of students")
        rollno = int(input("enter the students rollno "))
        mark = int(input("enter the students mark"))
        avg = mark//5
        w.writerow([name,rollno,mark,avg])

        option  = input("enter the yes to continue and no to break")
        if option.lower() == 'no':
            break
try:
    with open(filename,'r') as fh1:
        read = csv.DictReader(fh1)
        read = list(read)
        jsonfile = input("enter the json filename")
        with open(jsonfile,'w') as fh2:
            gett = json.dumps(read,indent = 0)
            fh2.write(gett)
except Exception as error:
    print(error)
