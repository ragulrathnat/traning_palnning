import pandas

file1 = pandas.read_csv("students.csv")
file2 = pandas.read_csv("section.csv")

print("-----------------minimum mark-------------")
mi = file1["MARK"].min()
print("minimum mark in file\n",file1.loc[file1["MARK"] == mi])

print("-----------------maximum mark------------")
mx =file1["MARK"].max()
print("maximum mark in file \n",file1.loc[file1["MARK"] == mx])

print("--------------sum----------------------------")
su = file1["MARK"].sum()
print("sum of mark",su)

print("-----------------------mean-------------")

me = file1["MARK"].mean()
print("students details greater than avg \n",file1.loc[file1["MARK"]>me])

print("----------------------condition-----------------")

final = pandas.merge(left = file1, right=file2, on = "ROLLno",how = "inner")
print(final.loc[final["Dept_name"] == "ECE"])

print("--------chcking is NUll----------")
print(file1[file1["AVG"].isnull()])

print("---------------------regex---------------")
print(final.loc[final["Dept_name"].str.contains("CSE")])


print("-----------------count----------------")
print(final.groupby("Dept_name").count())


print("--------------------number range-----------")

print(file1[file1["MARK"].between(300,450)])





#file1.rename(columns = {"Name":"strudent name"} ,inplace=True)
# # print(file1.head(11))

# # final = file2.groupby(" Dept_name").sum()
# # print(final)


# def find1(x):
#     if x > 5:
#         return "higher"
#     elif x < 5 and x > 3:
#         return "mid"
#     else:
#         return "lower"
    

# file2["range"] = file2["ROLLno"].apply(find1)
# #final2 = pandas.merge(left = file2,right= final,on = "ROLLno",how = "inner")
# #final= pandas.concat([file2,final])
# print(file2)

#(file1["ROLLno"].isin(file2["ROLLno"]).value_counts())


