import base64
n = input("enter the para")

encoded =base64.b64encode(n.encode('utf-8','replace'))

decoded = base64.b64decode(encoded.decode('utf-8'))


print("encoded value \n",encoded)

print("Decoded the para \n",decoded)


