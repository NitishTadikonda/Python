class X:
    def m1(self):
        print("in m1 of X")
class Y(X):
    def m2(self):
        print("in m2 of Y")
class Z(X):
    def m3(self):
        print("in m3 of Z")
print(X.__bases__)
print(Y.__bases__)
print(Z.__bases__)
y1 = Y()
y1.m1()
y1.m2()
z1 = Z()
z1.m3()
