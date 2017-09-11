import Test.A
from Test.B import b, f2
import Test.subpack1.C as p
from Test.subpack1.D import *

print(Test.A.a)
Test.A.f1()
print(b)
f2()
print(p.c)
p.f3()
print(d)
f4()
