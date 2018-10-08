import time
timenow=time.localtime(time.time())

print(timenow)

year,month,day,hour,minute,seconds=timenow[0:6]
print("---------------------------")
print("Year:",year,",Month:",month,",Day:",day,",Hour:",hour,",Minutes:",minute,",Seconds:",seconds)

print("-----------------------------")

for i in timenow:
  print(i)
print("-----------------------------")
print(timenow[0:10])
print("-----------------------------")

print(str(timenow[0]))

month={1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
print("-----------------------------")
print(month)
print("-----------------------------")
print("Today Date:")
print("_________________")
print("Month:")
for i in month:
  if(i==timenow[1]):
    print(month[i])

print("Year:",timenow[0])
print("Day:",timenow[2])
