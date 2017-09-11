'''class X:
    def m1(self):
        print("in m1 of X")
class Y:
    def m2(self):
        print("in m2 of Y")
class Z(X,Y):
    def m3(self):
        print("in m3 of Z")
print(X.__bases__)
print(Y.__bases__)
print(Z.__bases__)
z1 = Z()
z1.m3()
z1.m2()
z1.m1()

OR'''

class X:
    def m1(self):
        print("in m1 of X")
class Y:
    def m1(self):
        print("in m2 of Y")
class Z(X,Y):
    def m3(self):
        print("in m3 of Z")
print(X.__bases__)
print(Y.__bases__)
print(Z.__bases__)
z1 = Z()
z1.m3()
#z1.m2()#error it prints only first argument i.e X
z1.m1()



