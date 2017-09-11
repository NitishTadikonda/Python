class X:
    def m1(self):
        print("in m1 of x")
class Y:
    def m1(self):
        print("in m2 of Y")
class Z:
    def m3(Self):
        print("in m3 of Z")
class A(X,Y):
    def m4(self):
        print("in m4 of A")
class B(Y,Z):
    def m5(self):
        print("in m5 of B")
class C(A,B,Z):
    def m6(self):
        print("in m6 of C")
print(X.__bases__)
print(Y.__bases__)
print(Z.__bases__)
print(A.__bases__)
print(B.__bases__)
print(C.__bases__)
a = A()
a.m1()
a.m4()
'''c1 = C()
c1.m1()
c1.m2()
c1.m3()
c1.m4()
c1.m5()
c1.m6()'''


