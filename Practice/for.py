
n = int(input("Enter the height of the pyramid: "))

'''
to print
   *   
  ***  
 ***** 
*******'''
#starting multiple loops
for i in range(1,n+1): 
  for j in range(n-i):
      
    #prints the spacing
     print(" ",end='')
     
  #does the spacing on the left side
  for j in range(1,i):
    print("*",end='')
  for y in range(i,0,-1):
    print("*",end='')

  #does the spacing on the right side
  for x in range(n-i):
    print(" ",end='')



  #prints each line of stars
  print("")

print("")
print("")

'''
to print
*******
 ***** 
  ***  
   *   '''
#starting multiple loops
for i in reversed(range(1,n+1)): 
  for j in range(n-i):
      
    #prints the spacing
     print(" ",end='')
     
  #does the spacing on the left side
  for j in range(1,i):
    print("*",end='')
  for y in range(i,0,-1):
    print("*",end='')

  #does the spacing on the right side
  for x in range(n-i):
    print(" ",end='')



  #prints each line of stars
  print("")

print("")
print("")
'''
   *   
  **  
 *** 
****'''
   
#starting multiple loops
for i in range(1,n+1): 
  for j in range(n-i):
      
    #prints the spacing
     print(" ",end='')
     
  #does the spacing on the left side
  for j in range(1,i+1):
    print("*",end='')
  #does the spacing on the right side
  for x in range(n-i):
    print(" ",end='')

  print("")

print("")
print("")
'''

   *   
  **  
 *** 
****'''
for i in reversed(range(1,n+1)): 
  for j in range(n-i):
      
    #prints the spacing
     print(" ",end='')
      
  #does the spacing on the left side
  for j in range(1,i+1):
    print(" ",end='')

 
  #does the spacing on the right side
  for x in range(n-i+1):
    print("*",end='')
  #prints each line of stars
  print("")
