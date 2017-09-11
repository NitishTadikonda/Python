'''a = "Nitish"
b = reversed(a)#a[::-1]
if a == b:
    print("it is a palindrome" )
else:
    print("Not a palindrome")
      (or)'''

x = input("enter the string")
newstring = ''
index = len(x)-1
while index >= 0:
  newstring += x[index]
  index=index-1
print (newstring)
if x == newstring:
    print("palindrome")
else:
    print("Not a palindrome")
