

def m1(num, a):
    for k,v in enumerate(num):
        print("Index is " + str(k))
        print("value is " + str(v))
        a.append(v*v*v)




if __name__ == '__main__':
    n = [4,5,6,7]
    myArray = []

    m1(n,myArray)

    print(myArray[:])
    lastValue = myArray[-1]
    print("last value is " + str(lastValue))
    print(myArray[:-1])
