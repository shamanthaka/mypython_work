import csv
file = open("google_stock_data-1.csv",newline= '')
reader =csv.reader(file)

header = next(reader)
print(header)

data = [i for i in reader]

print(data[0])
