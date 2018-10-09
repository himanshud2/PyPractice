import dbConnector
def insertOperations():
	connection=dbConnector.getConnection()
	cursor=connection.cursor()
	query="INSERT INTO USER VALUES(%s,%s,%s)"
	value=["Mike","mike123","Manager"]
	cursor.execute(query,value)
	connection.commit()
	
	print("{0} record Inserted".format(cursor.rowcount))
	
insertOperations()