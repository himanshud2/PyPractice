#Not Working completely

import csv

file=open("newFile.csv","a")
mydict={"a":{0:"Mohit",1:"Kumar",2:22,3:"Manager"},"b":{0:"MK",1:"Singh",2:23,3:"HR"}}
writer=csv.writer(file)
#writer.writerows(data)
for key, value in mydict.items():
	for key1, value1 in value.items():
		writer.writerow([key,[key1, value1]])
file.close()