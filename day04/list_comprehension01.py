

def list_comprehension():
    my_p = (x * x for x in [1,2,3,4,5])
    print(my_p)
    return my_p

for i in list_comprehension():
    print("values " + str(i))


def list_comprehension2():
    my_list = [n for n in range(21) if n % 2 == 0]
    print(my_list)

list_comprehension2()