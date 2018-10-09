import dbConnector
def insertOperations(username,password,role):
	connection=dbConnector.getConnection()
	cursor=connection.cursor()
	query="INSERT INTO USER VALUES(%(username),%(password),%(role))"
	#query="INSERT INTO USER VALUES(%s,%s,%s)"
	value=[username,password,role]
	cursor.execute(query,value)
	connection.commit()
	
	print("{0} record Inserted".format(cursor.rowcount))
	
insertOperations("Jenny","jenny123","HR")

#not working