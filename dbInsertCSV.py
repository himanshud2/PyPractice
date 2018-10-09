import dbConnector
import csv
def displayAllData():
	connection=dbConnector.getConnection()
	query="select * from user"
	cursor=connection.cursor()
	cursor.execute(query)
	csvfile=open("dbInsertCS.csv","a")
	csvfile2=open("dbInsertCS2.csv","a")
	while True:
		result=cursor.fetchone()
		print(result)
		if(result!=None):
			list=[]
			list.append(result)
			print(list)
		else:
			break
		writer=csv.writer(csvfile)
		writer.writerows(list)
		writer2=csv.writer(csvfile2)
		writer2.writerows(result)
	csvfile.close()
	
displayAllData()