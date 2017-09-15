def print_msg(msg):
    a = 10 #global variable
    def printer():
        print(msg)#after deleting we can access only in the inner function.so it is called as a data hiding
        print(a)#providing global acess to the variable
        print(printer)
    return printer # returning the inner function address
print("Outer Function Address",print_msg)
a = print_msg("Hello")
print("Storing the inner function address:",a)
del print_msg #msg variable also should have to be deleted,outer function object deleted
a()

