import pandas
info = {'one': [1,2,3,4,5,6,6,7],'two':[9,8,6,54,3,21,5,4],
        'three':[43,5,2,4,2,4,5,3]
}

df =pandas.DataFrame(info)
print(df)

df['three'] = pandas.Series([1,2,3,4,5,6],index = [1,2,3,4,5,6])
df['four'] = df['three'] + df['one']

# del df['one']
# df.pop('two')
df = df.drop(0)
print(df)

info = {
    'x': [1,2,3,4,5,6],
    'y':[6,5,4,3,2,1]
}
info4 = pandas.DataFrame(info)
info1 = {
    'e' : [3,4,5,6,7,8],
    'r': [2,3,4,56,7,8]
}
info2 = pandas.DataFrame(info1)
info4._append(info2,ignore_index = True)
print(info4)
