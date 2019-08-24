from functools import reduce

data = [2, 3, 5, 7, 11, 17, 19, 23, 29]
multiplier = lambda x, y: x * y
mdata = reduce(multiplier, data)

print("Mulitiplication of data is " + str(mdata))