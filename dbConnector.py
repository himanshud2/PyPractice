import mysql.connector as driver
import datetime

def getConnection():
	try:
		mydb=driver.connect(host="localhost",database="pythonTest",user="root",password="root")
		if(mydb.is_connected()):
			print("connected {0}".format(mydb))
		return mydb
	except:
		print("Error in Connection")
		
		
connect=getConnection()
print(connect)