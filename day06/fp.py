from functools import reduce

values = [1,2,3,4,5,6,7,8,9]

even = list(filter(lambda x: x % 2 == 0, values))

print(even)

sum = reduce(lambda a, b: a + b, values)
print(sum)


name_lengths = list(map(len, ["Mary", "Isla", "Sam"]))

print(name_lengths)

squares = list(map(lambda x: x * x, [0, 1, 2, 3, 4]))

print(squares)


ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

#adults = filter(myFunc, ages)

adults = filter(lambda x: x < 18, ages)

for x in adults:
  print(x)












