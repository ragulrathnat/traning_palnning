import pandas

csvfile1 = input("enter the csvfile name")
csvfile2 = input("enter the csvfile name")

file1 = pandas.read_csv(csvfile1)
file2 = pandas.read_csv(csvfile2)

final = pandas.merge(left = file1, right = file2 , on = "Dept_id", how  = "inner")

final1 = final.groupby("Dept_id")['salary'].mean() 
final2 = pandas.merge(left = final1,right = file2 , on = "Dept_id" , how  = "inner")

final2.to_csv("amount.csv")