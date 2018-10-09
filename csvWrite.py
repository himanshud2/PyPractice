import csv

csvfile=open("Oct2018.csv","w")
csvData=[[1100,"Test","6-7-2018"],[1101,"Test2","2-3-2018"]]
writer=csv.writer(csvfile)
writer.writerows(csvData)

csvfile.close()