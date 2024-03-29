import multiprocessing
import time

def square_it(num):
    print('calculate square numbers.')
    for n in  num:
        time.sleep(0.2)
        print('square of {} is {} '.format(n,n*n))

def cube_it(num):
    print('calculate cube numbers.')
    for n in num:
        time.sleep(0.2)
        print('cube of {} is {} '.format(n,n*n*n))

def run_with_processes():
    arr = [2,3,8,9]
    start = time.time()

    p = multiprocessing.Process(target=square_it,args=(arr,))
    p2 = multiprocessing.Process(target=cube_it,args=(arr,))
    p.start()
    print('{} has started'.format('square_it'))
    p2.start()
    print('{} has started'.format('cube_it'))

    p.join()
    p2.join()

    end = time.time()
    print('time taken to complete the task:', str(end-start))


def run_without_processes():
    arr = [2,3,8,9]
    start = time.time()

    square_it(arr)
    cube_it(arr)

    end = time.time()

    print('time taken to complete the task:', str(end-start))


if __name__ == '__main__':
    run_with_processes()
    run_without_processes()