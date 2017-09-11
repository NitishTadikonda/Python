# Adding Elements to a set
vowels = {'a', 'e', 'i', 'u'}
print(type(vowels))
vowels.add('o')
print('Vowels are:', vowels)
vowels.add('a')
print('Vowels are:', vowels)

# Adding 'tuple' to a set
b = ('A', 'E', 'I', 'O', 'U')  # it comes as a set
vowels.add(b)
print('Vowels are:', vowels)

# copy Method
Vowels = vowels.copy()
print('Vowels After Copying:', Vowels)
a = {1, 2, 3, 4}
b = set(a)
b.add("5")
print("New numbers: ", b)

# deleting of a element
b.remove('5')  # remove(element)

print("After removing element:", b)

# using Pop()
print("Return value is", b.pop())  # by default it remove last element
print('B:', b)

# using Clear()
print('Vowels(before clear):', vowels)
vowels.clear()
print('vowels(after clear):', vowels)

# Discard(element)
print('numbers:', b)
b.discard(2)  # discarding the element 2
print('numbers:', b)

# Update
A = {'a', 'b'}
B = {1, 2, 3}

C = A.update(B)

print('A =', A)
print('B =', B)
print('result =', C)

# Adding elements of string and Dictionary to set
# updating with string
string_alphabet = 'abc'
numbers_set = {1, 2}

numbers_set.update(string_alphabet)

print('numbers_set =', numbers_set)
print('string_alphabet =', string_alphabet)

# update with dictionary
info_dictionary = {'key': 1, 2: 'lock'}
numbers_set = {'a', 'b'}

numbers_set.update(info_dictionary)
print('numbers_set =', numbers_set)

# Math Operations
a = {1, 2, 3, 4, 1, 2, 3}
print(a)  # it prints only (1,2,3)

a = {1, 2}
b = {2, 3, 4}
c = {4, 5, 6}

# Union(), | ==> Gives the all the elements in a,b,c
print('A U B =', (a | b))
print('B U C =', (b | c))
print('A U B U C =', a | b | c)
print('A U B U C  by using method (.union())=', a.union(b, c))  # using union() method
print('A U B U C by using method (.union())=', b.union(a, c))
print('A U B U C by using method (.union()) =', c.union(a, b))

# Intersection() , (&) ==> Gives the common elements of the sets
print(a.intersection(b, c))
print("Intersection of a and b:", a.intersection(b))

print("a & b :", (a & b))
print("Intersection of b & c:", (b & c))

'''difference() , (-) ==> The difference() method returns the difference of two sets which is also a set. It doesn't modify original sets.'''

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Equivalent to A-B
print(A.difference(B))  # gives only A elements
# Equivalent to B-A
print(B.difference(A))  # gives only B Elements

print("By using Operator(-):", A - B)
print("By using Operator(-):", B - A)

# Symmetric_Difference() ,(&) ==> Gives the elements except common elements

print(a.symmetric_difference(b))
print(b.symmetric_difference(c))

print(a ^ b)
print(b ^ c)

# Functions
x = {1, 2, 5, 4, 3}
for i in enumerate(x):
    print(i)
for i in enumerate(x,1):
    print(i)

print(max(x))
print(min(x))
print(len(x))
print(sorted(x))
print(sorted(x,reverse=True))
print(sum(x))