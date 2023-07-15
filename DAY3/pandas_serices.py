import pandas
from flask import Flask

x = pandas.Series([12,2,3,4,5,4], index = ['a','c','f','r','t','u'])
print(x)
print(x['a'])
print(x.index)
print(x.shape)
print(x.size)
print(x.empty)
print(x.hasnans)
print(x.nbytes)


# series function 
li = [1,2,3,4,5]
a = pandas.Series(li,name = 'val')
a.to_frame
print(a)