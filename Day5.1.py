import csv 
import requests 

resp = requests.get("https://api.publicapis.org/entries")
val = resp.json()

final = val["entries"]
print(final)

with open("finaloutput.csv","w") as file1:
    val1 = csv.writer(file1)
    val1.writerow(["API","Description","Auth","Category","Link"])
    for i in final:
        val1.writerow([i["API"],i["Description"],i["Auth"],i["Category"],i["Link"]])
































