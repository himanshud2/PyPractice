
#Not Working completely

import csv

file=open("newFile.csv","a")
data={"a":{0:"Mohit",1:"Kumar",2:22,3:"Manager"}
,"b":{0:"MK",1:"Singh",2:23,3:"HR"}}
writer=csv.writer(file)
writer.writerows(data)
file.close()
