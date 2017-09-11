class X:
    def m1(self):
        print("in m1 of X")
class Y(X):
    def m2(self):
        print("in m2 of Y")
class Z(Y):
    def m3(self):
        print("in m3 of Z")
print(X.__bases__)
print(Y.__bases__)
print(Z.__bases__)
z1 = Z()
z1.m1()
z1.m2()
z1.m3()
