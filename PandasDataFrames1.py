import pandas

year=[2001,2002,2003,2004]

delhipop=[20.01,40.09,13.50,45.50]
mumbaipop=[21.01,41.09,11.50,41.50]
bangalorepop=[23.01,11.09,31.50,61.50]

series1=pandas.Series(delhipop,index=year)
series2=pandas.Series(mumbaipop,index=year)
series3=pandas.Series(bangalorepop,index=year)

print(series1)

print(series2)

print(series3)

print("Data Frame")
myDataFrame=pandas.concat([series1,series2,series3],axis=1)	#Concatenation of Series 'Default' axis=0 (in single line)
print(myDataFrame)

#myDataFrame.columns(["Delhi","Mumbai","Bangalore"])		->Not Working

print(myDataFrame)