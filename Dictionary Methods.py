my_dict = {'name': 'Jack', 'age': 27}
# update value
# Output: {'age': 27, 'name': 'Jack'}
print(my_dict)

# add item
my_dict['address'] = 'Downtown'

# Output: {'address': 'Downtown', 'age': 27, 'name': 'Jack'}
print(my_dict)

squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
# Output: True
print(1 in squares)

# Output: True
print(2 not in squares)

# membership tests for key only not value
# Output: False
print(49 in squares)

# Methods
original = {1: 'one', 2: 'two'}

new = original.copy()
new = original  # copying

print('original:', original)
print('New:', new)

print(original.items())
print(original.keys())

original.pop(1)  # removing 1 element
print(original)

b = original.popitem()
print("original=", original)
print("Return value = ", b)
print(original.values())

# random sales dictionary
sales = {'apple': 2, 'orange': 3, 'grapes': 4}

values = sales.values()
print('Original items:', values)

# delete an item from dictionary
del [sales['apple']]
print('Updated items:', values)

d = {1: "one", 2: "three"}
d1 = {2: "two"}

# updates the value of key 2
d.update(d1)
print(d)

d1 = {3: "three"}

# adds element with key 3
d.update(d1)
print(d)

# Dictionary Comprehensions
squares = {x: x * x for x in range(6)}

# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares)
print(len(squares))

# using two lists for creating dictionary
D = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
print(D)

D = {x: x ** 2 for x in [1, 2, 3, 4]}
print(D)

D = {c: c * 4 for c in 'SPAM'}
print(D)

# Initialize dict from keys
D = dict.fromkeys(['a', 'b', 'c'], 0)
print(D)

# Same, but with a comprehension
D = {k:0 for k in ['a', 'b', 'c']}
print(D)