import time
import threading


class X(threading.Thread):
    def run(self):
        for i in range(1, 11):
            print(i)


class Y(threading.Thread):
    def run(self):
        time.sleep(15)
        for q in range(11, 16):
            print(q)


x1 = X()
x1.start()
y1 = Y()
y1.start()
for r in range(16, 21):
    print(r)
x1.join()
y1.join()
