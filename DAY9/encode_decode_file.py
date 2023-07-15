import base64 
import re

filename1 ="input.txt"
with open(filename1 , "r",encoding = "utf-8") as file1:
    data = file1.read()
    encoded =base64.b64encode(data.encode("utf-8",'ignore'))
    print("input file successfully encoded")
    with open("output.txt" , "wb") as file2:
        file2.write(encoded)
        print("encoded data write in output file ")


with open("output.txt","rb") as file3:
    print("decode information \n")
    for da in file3:
        decoded = base64.b64decode(da.decode("utf-8","repalce"))
        da_str = decoded.decode("utf-8")
        da = re.sub("\u3000"," ",da_str).rstrip("\n\r")
        print(da)
