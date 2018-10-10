import numpy

matrix=numpy.array([[1,2,3],[4,5,6],[7,8,9]])

print("Matrix:\n",matrix,"\n")

print("Order:",matrix.shape,"\n")

print("Matrix of Order 2X2:\n",matrix[:2,:2])

print("Order:",matrix[:2,:2].shape,"\n")

print("First 2 rows of matrix:\n",matrix[:2])

print("Column no:2\n",matrix[:,2])

print("Row no:1\n",matrix[0])

print(numpy.mean(matrix[0]))