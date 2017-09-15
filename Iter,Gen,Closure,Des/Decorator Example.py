def smart_divide(func):
    
   def inner(a,b):
      print("I am going to divide",a,"and",b)
      if b == 0:
         print("Whoops! cannot divide")
         return #return None

      return func(a,b)
   return inner

@smart_divide
def divide(a,b):
    return a/b

'''
#Without using @smart_divide
#uncomment this and comment the @smart_divide you will find the difference
p = divide
q = smart_divide(p)
print(q)
#q() #error
s = q(1,2) #because it is returning the divide function that's why we need to store that address in another variable and we call that function
print(s)
'''

#This is the example using decorator 
p = divide(2,5)
print(p)

q = divide(2,0)
print(q)
