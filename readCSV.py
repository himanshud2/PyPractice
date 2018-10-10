import csv
file=open("newFile.csv")
csv_reader = csv.reader(file, delimiter=',')
for row in csv_reader:
  print(row)
file.close()
