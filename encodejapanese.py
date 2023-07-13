import base64

with open("japanese.txt",'r',encoding='utf-8') as file1:
    data = file1.read()    
    encoded = base64.b64encode(data.encode("utf-8","ingore"))
    with open("outjapanese.txt","wb") as file2:
        file2.write(encoded)



with open("outjapanese.txt","rb") as file3:
     data = file3.read()
     decoded = base64.b64decode(data.decode("utf-8","ingore"))
     decode1 = decoded.decode("utf-8")
     print("japanese text successfully encode and decode\n ")
     print("decode japanese data\n", decode1)