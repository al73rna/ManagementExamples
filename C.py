__author__ = 'mohammadreza'
from threading import *



##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# tedadi thread be tedadi resource dastresi dashte va az anha estefade mikonand .
# baraye in manzur az yek semaphore ba meghdar avalie tedad resource ha estefade shode.

##<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

NUMBER_OF_RESOURCES = 10

class resource :
    def __init__(self):
        self.number = NUMBER_OF_RESOURCES
    def inc(self):
        self.number +=1
    def dec(self):
        self.number -=1

Mutex = Semaphore(value=NUMBER_OF_RESOURCES)


class A_THRD(Thread) :
    def __init__(self,_R):
        Thread.__init__(self)
        self.R = _R
    def run(self):
        while(True):

            Mutex.acquire()
            self.R.dec()
            print("Resource Available :",self.R.number)
            self.R.inc()
            Mutex.release()




MR = resource()

T1 = A_THRD(MR)
T2 = A_THRD(MR)
T3 = A_THRD(MR)
T4 = A_THRD(MR)
T1.start()
T2.start()
T3.start()
T4.start()