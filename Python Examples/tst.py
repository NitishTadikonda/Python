#using while and list
a_string = "nitish"
new_string = []
index = len(a_string)
while index:
    index -= 1                    # index = index - 1
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
    

    
