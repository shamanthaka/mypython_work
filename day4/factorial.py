

def my_fact(n):
    if n == 0:
        return 1
    return n * my_fact(n-1)

if __name__ == '__main__':
    print("Fact of n: " + str(my_fact(4)))