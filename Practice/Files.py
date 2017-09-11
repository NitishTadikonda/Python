'''x = open("Myfile.txt")
print(x)
print(x.read())
x.close()

x = open("Myfile.txt")
print(x.tell())
print(x.read())
print(x.tell())
x.close()

x = open("Myfile.txt")
print(x.tell())
x.seek(14)
print(x.tell())
print(x.read())
print(x.tell())
x.close()

x = open("Myfile.txt")
print(x.tell())
x.seek(2)
print(x.tell())
print(x.readline())
print(x.tell())
x.close()

x = open("Myfile.txt")
lines = x.readlines()
for i in lines:
    print(i)
x.close()

x = open("Myfile.txt")
x.write("\nHello\nNitish\welcome to My world")
x.close()'''

x = open("Myfile.txt","w")
x.write("\nHello\nNitish\nwelcome to My world")
x.close()