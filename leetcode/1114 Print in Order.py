# -*- coding: utf-8 -*-
import threading
from threading import Lock
import time
from queue import Queue
from typing import Callable


def printFirst():
    print('first')


def printSecond():
    print('second')


def printThird():
    print('third')


class Foo:
    def __init__(self):
        self.qub = Queue()
        self.quc = Queue()

    def first(self, printirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.

        printFirst()
        self.qub.put(0)

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        self.qub.get()
        printSecond()
        self.quc.put(0)

    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        self.quc.get()
        printThird()


# foo = Foo()
#
# t1 = threading.Thread(target=foo.first, args=([],))
# t2 = threading.Thread(target=foo.second,args=([],))
# t3 = threading.Thread(target=foo.third, args=([],))
#
# t1.start()
# t2.start()
# t3.start()

qu = Queue()


def ff():
    v = qu.get()
    print('v is', v)


# t = threading.Thread(target=ff)
# t.start()
#
# time.sleep(3)
#
# qu.put(30)

lock = Lock()
# lock.release()
# lock.release()

# lock.acquire()
# lock.acquire()

with lock:
    print('kk')

with lock:
    print('kk')
# print(lock)