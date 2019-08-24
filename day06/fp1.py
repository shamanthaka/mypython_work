from functools import reduce

values = [1,2,3,4,5,6,7,8,9]

"""even = list(filter(lambda x: x%2 == 0,values))

print(even)"""

def my_condition(x):
    if x%2 == 0:
        return True
    else:
        return False


even = list(filter(my_condition,values))

print(even)

#sum the given values, using with reduce

sum  = reduce(lambda x,y: x + y, values)

print(sum)

product = reduce(lambda x,y: x * y, values)

print(product)

product = reduce(lambda x,y: x / y, values)

print(product)


name_lengths = list(map(len, ["Mary", "Isla", "Sam"]))

print(name_lengths)



squares = list(map(lambda x: x * x, [0, 1, 2, 3, 4]))

print(squares)


