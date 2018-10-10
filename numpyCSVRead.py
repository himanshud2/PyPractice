import csv
import numpy

csvfile=open("winequality-white.csv")
reader=csv.reader(csvfile,delimiter=";")
list=[]
count=0
for row in reader:
	
	if(count!=0):
		intList=[]
		for i in row:
			x=float(i)
			intList.append(x)
		list.append(intList)
		count=1
	else:
		print(row)
		count=1

matrix=numpy.array(list)
print(matrix)
print(matrix.shape)

print("Mean of whole:",numpy.mean(matrix))
print("\nMatrix of 2X2:\n",matrix[:2,:2])
print("\nMean of 2X2:",numpy.mean(matrix[:2,:2]))

print("\nColumn No 1:\n",matrix[:,0])
print("\nMean of Column No 1:",numpy.mean(matrix[:,0]))

print("Sum of column 1 with column 2:",(matrix[:,0]+matrix[:,1])) #Result is List

print("Total Sum of column 1 with column 2:",(sum(matrix[:,0])+sum(matrix[:,1])))

print("Minimum element in Matrix:",numpy.min(matrix))