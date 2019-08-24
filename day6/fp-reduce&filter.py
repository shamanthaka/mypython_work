from functools import reduce
values = [1,2,3,4,5,6,7,8,9]
even = list(filter(lambda x:x % 2 == 0,values))
print(even)

sum = reduce(lambda a,b:a+b,values)
print(sum)