def make_multipler(x):
    def multipler(n):
        return x*n
    return multipler
a2 = make_multipler(2)
print(a2(3))

a = make_multipler(3)
print(a(3))

a = make_multipler(5)
b = a(2)
print(b)
