# -*- coding: utf-8 -*-


import threading
from queue import Queue


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n

        self.qu0 = Queue()
        self.qua = Queue()
        self.qub = Queue()

        self.qu0.put(1)
        self.cur = 1

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self) -> None:
        while self.cur < self.n + 1:
            # print('cur is', self.cur)
            _ = self.qu0.get()
            print(0, end='')

            if self.cur % 2 == 1:

                self.qua.put(self.cur)
            else:
                self.qub.put(self.cur)

            self.cur += 1
        self.qua.put(None)
        self.qub.put(None)

    def even(self) -> None:

        while True:
            v = self.qub.get()
            if v is None:
                break
            print(v, end='')
            self.qu0.put(0)

    def odd(self) -> None:
        while True:
            v = self.qua.get()
            if v is None:
                break
            print(v, end='')
            self.qu0.put(0)


ins = ZeroEvenOdd(100)

t = threading.Thread(target=ins.zero, daemon=False)
t2 = threading.Thread(target=ins.even, daemon=False)
t3 = threading.Thread(target=ins.odd, daemon=False)

t.start()
t2.start()
t3.start()


def m():
    while True:
        pass


t4 = threading.Thread(target=m, daemon=True)

t4.start()

# print('ok')
