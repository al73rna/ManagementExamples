__author__ = 'mohammadreza'

from threading import *

##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# yek tabe be onvane fazaye moshtarak entekhab shode va tavasote thread haye mokhtalef ejra mishavad .
# moshahede mikonid ke tartibe ejraye dasturat taghir nemikonad
# baraye in manzur az yek mutex estafe shode ta nahie bohrani moshakhas shavad.

##<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

def MutualMemory():
    A = 3
    print("a",A-1)
    print("b",A-2)
    print("c",A-3)

Mutex = Lock()

class A_THRD(Thread) :
    def run(self):
        while(True):
            Mutex.acquire()
            MutualMemory()
            Mutex.release()

T1 = A_THRD()
T2 = A_THRD()
T3 = A_THRD()
T4 = A_THRD()

T1.start()
T2.start()
T3.start()
T4.start()