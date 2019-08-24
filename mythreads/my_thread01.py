
import threading
import time

def sleeper(n, name):
    print('Hi, I am {}. Going to sleep for {} seconds\n'.format(name,n))
    time.sleep(n)
    print('{} has woken up from sleep\n'.format(name))


if __name__ == '__main__':
    t = threading.Thread(target=sleeper, name='thread2', args=(6, 'thread1'))
    t.start()
    t.join()
    print("Main thread is executed. ")