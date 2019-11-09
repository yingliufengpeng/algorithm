# -*- coding: utf-8 -*-

# import threading
#
# lock = threading.Lock()
#
# lock.acquire()
# # lock.acquire()
# lock.release()

r15, r5, r3 = [], [], []
r = []
for i in range(1, 100 + 1):
    if i % 5 == 0:
        r.append(i)

    if i % 5 == 0 and i % 15 != 0:
        r5.append(i)

    if i % 3 == 0 and i % 15 != 0:
        r3.append(i)

    if i % 15 == 0:
        r15.append(i)

print(r3)
print(r5)
print(r15)
print(r)

print(len(r5) + len(r15) == len(r))