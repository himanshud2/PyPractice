def add(x,y):
  num1=int(x)
  num2=int(y)
  return num1+num2

def subtract(x,y):
  num1=int(x)
  num2=int(y)
  return num1-num2

def multiply(x,y):
  num1=int(x)
  num2=int(y)
  return num1*num2

def division(x,y):
  num1=int(x)
  num2=int(y)
  return num1/num2

while True:
  print("-------------Menu-------------")
  print("1.Add")
  print("2.Subtract")
  print("3.Multiply")
  print("4.Division")
  print("5.Exit")
  choice=input("Enter the choice:")
  if(int(choice)==1):
    x=input("Enter Number1:")
    y=input("Enter Number2:")
    print(add(x,y))
  elif(int(choice)==2):
    x=input("Enter Number1:")
    y=input("Enter Number2:")
    print(subtract(x,y))
  elif(int(choice)==3):
    x=input("Enter Number1:")
    y=input("Enter Number2:")
    print(multiply(x,y))
  elif(int(choice)==4):
    x=input("Enter Number1:")
    y=input("Enter Number2:")
    print(division(x,y))
  elif(int(choice)==5):
    sys.exit()
