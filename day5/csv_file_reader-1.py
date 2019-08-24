import csv

file = open("google_stock_data-1.csv",newline='')
reader = csv.reader(file)

header = next(reader)
print(header)
data =[row for row in reader]

print(data[0])

#2nd method
