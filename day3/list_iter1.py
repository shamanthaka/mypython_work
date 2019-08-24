
friends = ["Kevin", "Karen", "Jim", "Venkatram","Srijan"]

def iter1():
    for i, val in enumerate(friends):
        print(i, val)


def iter2():
    iter = friends.__iter__()

    while True:
        try:
            print(iter.__next__())
        except StopIteration:
            break

if __name__ == '__main__':
    iter1()
    print("*************")
    iter2()
