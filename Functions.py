def myfunc(a, b):
    print("hello")
    c = a + b
    print(c)
    return c


print(myfunc)
c = myfunc(1, 2)
print(c + 8)  # using the return in the another variable
var = myfunc  # accessing address of the my func to variable
var(4, 5)
print(var)
