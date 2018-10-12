import pandas

dataframe=pandas.read_csv("winequality-white.csv",sep=';')

print(dataframe)
print("===================================================")
print(dataframe.alcohol)
print("===================================================")

data1=dataframe['fixed acidity']
print(data1)
print("===================================================")
print(data1.sort_values())