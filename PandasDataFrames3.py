import pandas

#pandas	->read_table()
# read_csv(,sep='')

dataFrame=pandas.read_csv("https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv")

#print(dataFrame)

newdataFrame=dataFrame.head(20)	#Read First 20 records
print("=================================")
print(newdataFrame)
newdataFrame1=dataFrame.tail(20)	#Read last 20 records
print("=================================")
print(newdataFrame1)
print("=================================")
print(newdataFrame.describe())