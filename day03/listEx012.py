
friends = ["Kevin", "Karen", "Jim", "Venkatram","Srijan"]
print(friends)
print("sort: ")
friends.sort()
print(friends)
print("from last index: ")
print(friends[-1])
print('copying to another list:')
friends2 = friends.copy()
print(friends2)

lucky_numbers = [42, 8, 15, 23, 4]
print("sort numbers list: ")
lucky_numbers.sort()
print(lucky_numbers)

print("list with index")
print(friends[0])

print("range 0, 3")
print(friends[0:3])
print("range 1, end")
print(friends[1:])

#list functions

friends.extend(lucky_numbers)
print("merged friends and numbers")
print(friends)
print("appended at the end")
friends.append("Vasu")

print(friends)
print("inserted at a perticular index:")
friends.insert(1, "Ram")
print(friends)
print("removed")
friends.remove("Jim")

print(friends)
print("after pop: ")
friends.pop()

print(friends)
print("getting index from value:")
print(friends.index("Srijan"))







