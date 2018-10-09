import dbConnector

def displayAllData():
	connection=dbConnector.getConnection()
	query="select * from user"
	cursor=connection.cursor()
	cursor.execute(query)
	while True:
		result=cursor.fetchone()
		if(result!=None):
			print(result)
		else:
			break
		
displayAllData()