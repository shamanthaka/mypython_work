from multiprocessing import Pool
import time

def f(n):
    sum = 0
    for x in range(1000):
        sum += x * x
    return sum

def run_with_processes():
    t1 = time.time()
    p = Pool()
    result = p.map(f, range(100000))  # function f is called 100,000 times
    print("Result is ", result)
    p.close()
    p.join()
    t2 = time.time()
    print("POOL processing Time taken ", (t2 - t1))




def run_with_out_process():
    t1 = time.time()
    result = []

    for x in range(100000):
        result.append(f(x))

    print("Result is ", result)
    t2 = time.time()
    print("Serial processing is time taken ", (t2 - t1))


if __name__ == '__main__':
    run_with_processes()
    run_with_out_process()
