import threading
import time

class ThreadSynchronizationEg(threading.Thread):

    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):
        lock.acquire()
        self.process()
        lock.release()


    def process(self):
        for n in range(10):
            #print(f"{self.name} it's value is {n}")
            print("{} it's value is {} ".format(self.name, str(n)))
            #print(self.name +"it's value is " + str(n))
            print("\n")



if __name__ == '__main__':
    lock = threading.Lock()

    t1 = ThreadSynchronizationEg("thread 1")
    t2 = ThreadSynchronizationEg("thread 2")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("main thread exited.")