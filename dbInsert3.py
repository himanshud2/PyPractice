import dbConnector
def insertOperations(username,password,role):
	connection=dbConnector.getConnection()
	cursor=connection.cursor()
	
	query="INSERT INTO USER (username,role) VALUES(%s,%s)"
	#query="INSERT INTO USER VALUES(%s,%s,%s)"	->working
	
	value=[username,role]
	cursor.execute(query,value)
	connection.commit()
	
	print("{0} record Inserted".format(cursor.rowcount))
	
insertOperations("Kyle","kyle123","HR")

#not working



#add_salary = ("INSERT INTO salaries "
#              "(emp_no, salary, from_date, to_date) "
#              "VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")
