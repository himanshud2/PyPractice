import pandas

year=[2001,2002,2003,2004]

delhipop=[20.01,40.09,13.50,45.50]
mumbaipop=[21.01,41.09,11.50,41.50]

delhiSeries=pandas.Series(delhipop,index=year)

mumbaiSeries=pandas.Series(mumbaipop,index=year)	#year should be a list and of same length as mumbaipop

mySeries=delhiSeries+mumbaiSeries	#Series Addition

year2=[2001,2002]

noidapop=[12.30,43.30]

newSeries=pandas.Series(noidapop,index=year2)

print(mySeries)

totalSeries=newSeries+mumbaiSeries	#Outputs NaN for the miss matching indices if the series are not of equal length

print(totalSeries)

print(mumbaiSeries[2001])


print(delhiSeries>40)

dSeries=delhiSeries[delhiSeries>40]

print(dSeries)
print("=========================")
print(totalSeries.isnull())
print("=========================")
print(totalSeries.notnull())
print("=========================")
print(totalSeries.dropna())
print("=========================")
print(totalSeries.fillna(999))
print("=========================")
print(delhiSeries.sort_values())