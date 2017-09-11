x = [10, 20, 30, 40, 50, 60, 70]
print(x)

y = x.copy()
print("this is the copy list", y)

print("the count of number", x.count(70))

print(x.index(30))

x.insert(3, 80)  # inserting element in a index
print(x)

x.pop(5)  # pop the element with the index

x.sort(reverse=True)  # reverse operation
print(x)
x.sort()  # it will sort in ascending order
print(x)

y = [90, 100, 120]  # we can extend tuple and set
x.extend(y)
print(x)
language_tuple = ('Spanish', 'Portuguese')
x.extend(language_tuple)
print(x)

x.remove(120)  # here element will be removed
print(x)

a = [1, 2]
b = [3, 4]
a += b
a.reverse()
print('a = ', a)

a.clear()
print(a)
# list comprehension
pow2 = [2 ** x for x in range(10)]
# Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
print(pow2)

# list membership Test
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
# Output: True
print('p' in my_list)


# enumerate Function
x = ['a', 'b', 'c']
y = enumerate(x)
print(type(y))
print(list(y))
y = enumerate(x, 1)  # changing the default value from 0 to 1
print(list(y))
for i in enumerate(x):
    print(i)

print(len(x))

# converting the data types into list
# empty list
print(list())

# vowel string
vowelString = 'aeiou'
print(list(vowelString))

# vowel tuple

vowelTuple = ('a', 'e', 'i', 'o', 'u')
print(list(vowelTuple))

# vowel list
vowelList = ['a', 'e', 'i', 'o', 'u']
print(list(vowelList))

x = [10, 100, 200, 20, 550]
y = max(x)
z = min(x)
print(y)
print(z)
print(sorted(x))
# sorting in reverse order
print(sorted(x, reverse=True))

# sum function
y = sum(x)
print(y)
