# vowels tuple
vowels = ('a', 'e', 'i', 'o', 'i', 'o', 'e', 'i', 'u')

# count element 'i'
count = vowels.count('i')

# print count
print('The count of i is:', count)
# index
# element 'e' is searched
index = vowels.index('e')

# index is printed
print('The index of e:', index)

# Built in Functions
vowels = (1, 2, 3, 4, 6, 5, 7,9)
print(len(vowels))
print(max(vowels))
print(min(vowels))
print(sorted(vowels))
print(sorted(vowels,reverse=True))
print(sum(vowels))
for i in enumerate(vowels):
    print(i)
for i in enumerate(vowels,1):
    print(i)