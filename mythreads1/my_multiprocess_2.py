import  multiprocessing
import  time

squre_result = []
def square_it(num):
    global squre_result
    print('calculate square numbers. ')
    for n in num:
        time.sleep(0.2)
        square = n*n
        print('square of {} is {} '.format(n,square))
        squre_result.append(square)


    print("within process", squre_result)

def run_with_processes():
    arr = [2, 3, 8, 9]
    start = time.time()
    square_it(arr)
    end = time.time()
    print('time takes to complete the task :',str(end-start))


if __name__ == '__main__':
    run_with_processes()