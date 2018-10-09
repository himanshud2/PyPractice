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
			writer=csv.writer(csvfile)
			writer.writerows(list)		#-> writes according to each list object
			print(list)
			#writer2=csv.writer(csvfile2)
			#writer2.writerows(result)		->writes according to tuple individual content in csv file(new Line)
		else:
			break
		
	csvfile.close()
	
displayAllData()