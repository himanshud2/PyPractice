class MyException(Exception):
	pass
	
def getInput():
	x=input("Enter Number1:")
	if(int(x)<0):
		raise MyException("{0} is not Positive Number".format(x))
	else:
		return x

def display():
	try:
		a=getInput()
		print(a)
	#except MyException:
	#	print(MyException)
	except MyException as e:
		print(e)
	finally:
		print("BYE!")

display()