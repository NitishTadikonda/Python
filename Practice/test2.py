class X:
    '''destructor'''
    def __init__(self):
        print("in constructor of x")
    def __del__(self):
        print("In destructor of X")
    def m1(self):
        print("in m1 of x")
   
        
x1 = X()
print(x1)
x1.m1()
x2 = x1
print(x2)
x2.m1()
x3 = x2
print(x3)
x3.m1()
x1 = X()
print(x1)
x1.m1()
x2 = X()
print(x2)
x2.m1()
x3 = X()
print(x3)
x3.m1()
