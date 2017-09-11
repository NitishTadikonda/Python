#check Whether give number is positive number or not by using if-elif-else
n = int(input("enter the number"))
if n >0:
    print("positive number")
elif n==0:
    print("Zero")
else:
    print("Negative number")

#checking Whether Positive number or not  by using if-else    
n = int(input("enter the number"))
if n >0:
    if n==0:
        print("Zero")
    else:
        print("positive number")
else:
    print("Negative number")

#finding Even Or Odd
n = int(input("enter the number for odd or even"))
if (n % 2) == 0:
    print("Number is Even")
else:
    print("Odd Number")

# finding leap year or not
n = int(input("Enter the Year"))
if (n %4) ==0:
    if(n % 100) ==0:
        if(n% 400) == 0:
            print("{0} a leap year".format(n))
        else:
            print("{0} is not a leap year".format(n))
    else:
        print("{0} is a leap year".format(n))
else:
    print("{0} Not leap Year".format(n))

#factorial of a Given number
n  = int(input("enter a number for factorial"))
m = 1
if n<0:
    print("Factorial is not possible")
elif n==0:
    print ("the zero facatorial is 1")
else:
    for i in range(1,n+1):
        m = m*i
    print("The factorial of given %d is %d"%(n,m))


#checking prime number or not
n =  int(input("enter the number for prime number or not"))
if n>1:
    for i in range(2,n):
        if (i%2)==0:
            print("not a prime number")
            break
    else:
        print("it's a prime number")
else:
    print("is not a prime number")


#prime numbers for a given range
lower = 0
upper = int(input("Enter upper range: "))
print("Prime numbers between",lower,"and",upper,"are:")

for i in range(lower,upper + 1):
   # prime numbers are greater than 1
   if i > 1:
       for j in range(2,i):
           if (i % j) == 0:
               break
       else:
           print(i)
           
# Program to find armstrong Number or not
print("Enter any number for checking Armstrong Number: ")
number = int(input())
temp = int(number)
Sum = 0
 
while(temp >0):
    rem  = temp % 10 
    Sum += (rem **len(str(number)))
    temp = temp//10
if number == Sum:
    print ("Armstrong Number")
else:
    print ("Not an Armstrong Number")


# Program to check Armstrong numbers in certain interval
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
for num in range(lower, upper + 1):
   # initialize sum
   sum = 0
   # find the sum of the cube of each digit
   temp = num
   while temp > 0:
       a = temp % 10
       sum += a ** len(str(num))
       temp //= 10

   if num == sum:
       print(num)

#reversing of a string
#using while and list
a_string = "nitish"
new_string = []
index = len(a_string)
while index:
    index -= 1       # index = index - 1
    new_string.append(a_string[index])
print(''.join(new_string))
      #or
#using conta and While
a_string ='Nitish'
new_string = ''
index = len(a_string)
while index:
    index -= 1                    # index = index - 1
    new_string += a_string[index] # new_string = new_string + character
print(new_string)
      #or
#slicling operation 
a_string ="nitish"
print(a_string[::-1])

#using concatenation
a ="nitish"
c=''
print(a)
for i in range(len(a)):
    c=c+a[len(a)-i-1]
print(c)

#by using list
a = 'nitish'
c=[]
for i in range(len(a),0,-1):
    c.append(a[i-1])
print (''.join(c))

#prints line by line
a ='nitish'
i= len(a)-1
while i>=0:
    print(a[i])
    i = i-1
    

    
