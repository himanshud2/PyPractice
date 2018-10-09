import dbConnector
def insertOperations():
	connection=dbConnector.getConnection()
	cursor=connection.cursor()
	query="INSERT INTO USER VALUES('MAX','MAX123','MANAGER')"
	cursor.execute(query)
	connection.commit()
	
	print("{0} record Inserted".format(cursor.rowcount))
	
insertOperations()