
name_lengths = list(map(len,["Mary", "Isla","sam"]))

print(name_lengths)

squares = list(map(lambda x:x *x ,[0,1,2,3,4,5,6]))

print(squares)

def myFunc(x):
    if x < 18:
        return False
    else:
        return True


ages = [23,45,1,3,17,20,19,5]

adults = filter(lambda x:x<18,ages)

for x in adults:
    print(x)
