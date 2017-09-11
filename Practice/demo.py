'''#1
c = []
for i in range(1500,2700):
    if i % 7 ==0 and i%5 == 0:
        #print("x is{0} and x divided by 7 is{1} and multiply of 5".format(i,(i//7)))
        c.append(i)
print(c)

#2
temp = float(input("enter the temperature you like to convert"))
k = input("Enter the temprature kind (F or c)")
degree = int(temp)

if k == 'C' or k == 'c':
    result = int(round((9 * degree) /5 + 32))
    b = "Fahrenheit"
elif k == 'F' or k == 'f':
    result = int(round((degree - 32) * 5 / 9))
    b = "Celsius"
else:
    print("input proper format")
print("The Temperature in %s is %d degrees"%(b,result))

#3 guessing a random number
import random
num = random.randint(1,10)
guess_num =0
while num !=guess_num:
    guess_num = int(input("Guess a number Guess a number between 1 and 10 until you get it right : "))
print('Well guessed!')'''

'''4 printing the pattern
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
n =5
for i in range(n):
    for j in range(i):
        print('*',end='')
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('*',end = '')
    print(' ')
    
n=3
for i in range(n):
    print(i*"*")
while i>0:
    i-=1
    print(i*"*")

n = 6
count = 0
for i in range(n):
    x = '*'
    count+=1
    print(x*count)
for i in range(n):
    x ='*'
    count-=1
    print(x*count)
#5    
x = input("Enter the word to reverse")
x = x[::-1]
print(x)

x = input("enter the word")
c = ''
for i in range(len(x)):
    c = c+x[len(x)-1-i]
print(c)

d =[]
for i in range(len(x),0,-1):
    d.append(x[i-1])
print(''.join(d))

#6
lower  =int(input("enter the lower range"))
upper = int(input("enter the upper range"))
count_odd = 0
count_even = 0
for i in range(lower,upper+1):
    if i %2==0:
        count_even+= 1
    else:
        count_odd+=1
print("Number of even numbers %d"%(count_even))
print("Number of odd numbers %d"%(count_odd))
#7
datalist = [1452, 11.23, 1+2j, True, 'Nitish', (0, -1), [5, 12], {"class":'V', "section":'A'}]
for i in datalist:
    print(i,type(i))

#8
for x in range(6):
    if (x == 3 or x==6):
        continue
    print(x,end=' ')# in case of 2.7 print x, 
print("\n")

#9
n = int(input("enter the number of terms"))
first = 0
second =1
for i in range(n):
    if i<=1:
        next = i
    else:
        next = first+second
        first = second
        second = next
    print(next)
#or
first = 0
second =1
while second<50:
    print(second)
    first,second = second,first+second

#10
for i in range(50):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
        continue
    elif i %3 == 0:
        print("Fizz")
        continue
    elif i %5 ==0:
        print("Buzz")
        continue
    else:
        print(i) '''

        
    

















    
