from time import sleep
from threading import *


class Thread1(Thread):

    def run(self):
        for i in range(100):
            print("Thread1")
            sleep(0.3)


class Thread2(Thread):

    def run(self):
        for i in range(100):
            print("Thread2")
            sleep(0.3)


t1 = Thread1()
t2 = Thread2()

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()

print("Over...")
