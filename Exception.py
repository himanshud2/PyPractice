number=input("Enter the Number:")
try:
  x=int(number)
  print("Number:",number)
except:
  print("Invalid Input")
finally:
  print("BYE!!")
