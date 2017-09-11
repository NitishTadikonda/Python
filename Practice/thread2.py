import time
import threading


class X(threading.Thread):
    def run(self):
        lc.acquire()
        f1("Nitish")
        lc.release()


class Y(threading.Thread):
    def run(self):
        lc.acquire()
        f1("Tadikonda")
        lc.release()


def f1(msg):
    print("[hello[", msg)
    time.sleep(20)
    print("]Welcome to Python world]")

lc = threading.Lock
x1 = X()
x1.start()
y1 = Y()
y1.start()
x1.join()
y1.join()
