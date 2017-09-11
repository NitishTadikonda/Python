'''a = [5, 5, 2, 55, 24, 21]
b = [5, 6, 7, 8, 2, 12, 24]
c = []
a = set(a)
b = set(b)
#print(a ^ b)
c.append(a ^ b)# prints the except those that are common in both
print(c)
#c.append(a | b) # all the elements in the set
#print(c)
c.append(a & b) # prints the common elements
print(c)'''
a = [5, 5, 2, 55, 24, 21]
b = [5, 6, 7, 8, 2, 24]
c = []
for i in a:
    if i not in b:
        c.append(i)
for i in b:
    if i not in a:
        c.append(i)
print(c)

