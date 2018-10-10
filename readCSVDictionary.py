
import csv

file=open("newFile.csv","a")

reader=csv.reader(file)
for rows in reader:
	print(rows)
	
file.close()