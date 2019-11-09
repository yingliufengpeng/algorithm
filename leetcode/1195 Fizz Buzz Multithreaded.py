# -*- coding: utf-8 -*-
from collections import Callable
import threading


def printFizz():
    print('fizz')


def printBuzz():
    print('buzz')


def printFizzBuzz():
    print('fizzbuzz')


def printNumber(n):
    print(n)


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n

        self.lockA = threading.Lock()
        self.lockB = threading.Lock()
        self.lockC = threading.Lock()
        self.lockD = threading.Lock()

        self.lockA.acquire()
        self.lockB.acquire()
        self.lockC.acquire()

        self.cur = 1

        self.r3, self.r5, self.r15 = [], [], []

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 15 != 0:
                self.r3.append(i)
            if i % 5 == 0 and i % 15 != 0:
                self.r5.append(i)
            if i % 15 == 0:
                self.r15.append(i)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            self.lockA.acquire()

            if self.n < 3:
                break

            printFizz()
            self.lockD.release()

            if self.cur == self.r3[-1]:
                # print('A')
                break

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            self.lockB.acquire()
            if self.n < 5:
                break
            # print('fsfsdfs')
            printBuzz()

            self.lockD.release()
            if self.cur == self.r5[-1]:
                # print('B')
                break

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            self.lockC.acquire()
            # print('fff')
            if self.n < 15:
                break
            printFizzBuzz()

            self.lockD.release()

            if self.cur == self.r15[-1]:
                # print('C')
                break

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:

        for i in range(1, self.n + 1):
            self.lockD.acquire()
            # print('cur is', i)
            self.cur = i
            if i % 3 == 0 or i % 5 == 0:

                if i % 3 == 0 and i % 5 == 0:

                    self.lockC.release()
                    self.lockD.acquire()
                    self.lockD.release()
                    # print(i)

                elif i % 3 == 0:
                    self.lockA.release()
                    self.lockD.acquire()
                    self.lockD.release()
                    # print(i)

                elif i % 5 == 0:
                    self.lockB.release()
                    self.lockD.acquire()
                    self.lockD.release()

            else:
                printNumber(i)
                self.lockD.release()

        # while True:
        #     locks = [self.lockA, self.lockB, self.lockC]
        #     for lock in locks:
        #         if lock.locked():
        #             lock.release()
        # self.lockB.release()
        if self.n < 3:
            self.lockA.release()
            self.lockB.release()
            self.lockC.release()

        elif self.n < 5:
            self.lockB.release()
            self.lockC.release()

        elif self.n < 15:
            self.lockC.release()


s = FizzBuzz(18)
ta = threading.Thread(target=s.fizz, args=(printFizz,))
tb = threading.Thread(target=s.buzz, args=(printBuzz,))
tc = threading.Thread(target=s.fizzbuzz, args=(printFizzBuzz,))
td = threading.Thread(target=s.number, args=(printNumber,))

ts = [ta, tb, tc, td]

for t in ts:
    t.start()
