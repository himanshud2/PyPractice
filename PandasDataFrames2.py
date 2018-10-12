import pandas

year=[2001,2002,2003]

myDictionary={"Delhi":[1,2,3],"Mumbai":[4,5,6],"Bangalore":[6,7,8]}

mydataFrame=pandas.DataFrame(myDictionary,index=year)

print(mydataFrame)

print(mydataFrame.shape)

print(mydataFrame.describe())	#includes mean,count,etc