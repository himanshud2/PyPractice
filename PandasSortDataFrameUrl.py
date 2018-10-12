import pandas

dataFrame=pandas.read_csv("https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv")

newdataFrame=dataFrame.tail(20)

print("================================================")
print(newdataFrame)

print("================================================")
print(newdataFrame.sort_values("City",ascending=False))
print("================================================")
Data2=newdataFrame["Colors Reported"]
booleanSeries=Data2.notnull()

print(newdataFrame[booleanSeries])

print("=================================================")
DataTime=newdataFrame.Time
print("=================================================")
print(DataTime.sort_values())
print("=================================================")
print(newdataFrame.sort_values("Time"))

print("================================================")
print(newdataFrame.sort_values("Colors",ascending=False))

data1=newdataFrame.City
print("================================================")
print(data1)

sortData1=data1.sort_values()
print(sortData1)
