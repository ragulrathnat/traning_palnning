

'''Program which gets input from the user and writes it in a file. The program needs to accept input 
text and file path
'''
filename = input("enter the file name to write")

try:
    fh = open(filename,'w')
    data = input("enter the imformation to write in file")
    fh.write(data)
    fh.close()
except Exception as error:
    print(error)


try:
    fh = open(filename,'r')
    print(fh.read())
    fh.close()
except Exception as error:
    print(error)