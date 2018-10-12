import pandas

#print(pandas)

myList=[101,102]

myIndex=pandas.Series(myList)

print(myIndex)

cities=['Delhi','Mumbai']

mySeries=pandas.Series(cities,index=myList)

print(mySeries)
