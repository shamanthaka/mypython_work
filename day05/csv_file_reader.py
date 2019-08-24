

"""file = open("google_stock_data.csv")
for line in file:
    print(line)
    
    """

lines = [line for line in open("google_stock_data.csv")]

print(lines[0])

print(lines[0].strip())


csv = lines[1].strip().split(",")
print(csv)

for value in csv:
    print(value)