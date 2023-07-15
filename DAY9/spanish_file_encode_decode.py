import base64

with open("inspanish.txt","r",encoding="utf-8") as file1:
    data = file1.read()
    encoded = base64.b64encode(data.encode("utf-8","ignore"))

    with open("outspanish.txt","wb") as file2:
        file2.write(encoded)


with open("outspanish.txt","rb") as file3:
    data = file3.read()
    decoded = base64.b64decode(data.decode("utf-8","ignore"))
    decode_str= decoded.decode("utf-8",'ignore')
    print("spanish text is successfully encoded and decode\n")
    print("decode spanish text ",decode_str)