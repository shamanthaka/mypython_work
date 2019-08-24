import threading
import time

class MyThread(threading.Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        for i in range(5):
            time.sleep(2)
            print(f"{self.name} it's value is {i}\n")


if __name__ == '__main__':
    t1 = MyThread("MyThread1")
    t1.start()

    t2 = MyThread("MyThread2")
    t2.start()
