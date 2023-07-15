import base64
with open("inchinese.txt", "r",encoding="utf-8") as file1:
    data = file1.read()
    encoded = base64.b64encode(data.encode("utf-8","ignore"))
    with open("outchinese.txt","wb") as file2:
        file2.write(encoded)
    

with open("outchinese.txt","rb") as file2:
    data = file2.read()
    decoded = base64.b64decode(data.decode("utf-8","ignore"))
    decoded_str = decoded.decode("utf-8","ignore")
    print("chinese text is successfully encoded and decoded\n")
    print("decode chenese text \n",decoded_str)
    