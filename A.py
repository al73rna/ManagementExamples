__author__ = 'mohammadreza'
from threading import *


##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# yek adad dar fazaye hafeze be onvane resource tarif shode ke 2 thread consumer va supplier darad .
# baraye in manzur az yek mutex estafe shode ta nahie bohrani moshakhas shavad.

##<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

class resource :
    def __init__(self):
        self.number = 500
    def inc(self):
        self.number += 1
    def dec(self):
        self.number -= 1

Mutex = Lock()


class A_THRD(Thread) :
    def __init__(self,_R):
        Thread.__init__(self)
        self.R = _R
    def run(self):
        while(True):
            Mutex.acquire()
            self.R.inc()
            Mutex.release()
            print("Value Increased to :",self.R.number)

class B_THRD(Thread) :
    def __init__(self,_R):
        Thread.__init__(self)
        self.R = _R
    def run(self):
        while(True):
            Mutex.acquire()
            self.R.dec()
            Mutex.release()
            print("Value Decreased by :",self.R.number)




mutex = Lock()

MR = resource()

T1 = A_THRD(MR)
T2 = B_THRD(MR)
T3 = A_THRD(MR)
T4 = B_THRD(MR)
T1.start()
T2.start()
T3.start()
T4.start()