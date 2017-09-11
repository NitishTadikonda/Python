import time
import threading


class X(threading.Thread):
    def run(self):
        f1("Nitish")


class Y(threading.Thread):
    def run(self):
        f1("Tadikonda")

def f1(msg):
    print("[hello[",msg)
    time.sleep(20)
    print("]Welcome to Python world]")
x1 = X()
x1.start()
y1 = Y()
y1.start()
x1.join()
y1.join()