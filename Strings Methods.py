x = "python is awesome."

# capitalize()
a = x.capitalize()
print('Old String: ', x)
print('Capitalized String:', a)

# center
b = x.center(24)
print("Centered String", b)
new_string = x.center(24, '*')  # Center() Method With * fill char
print("Centered String: ", new_string)

print("Uppercase string:", x.casefold())

# count
count = x.count('is')
print("The count is:", count)
count = x.count('i', 8, 18)  # count after first 'i' and before the last 'i'
print("The count is:", count)

# ends with
text = "Python is easy to learn."
result = text.endswith('to learn')

print(result)  # returns False
result = text.endswith('to learn.')

print(result)  # returns True
result = text.endswith('Python is easy to learn.')

print(result)  # returns True
result = text.endswith('learn.', 7)
print(result)

# Both start and end is provided
# start: 7, end: 26
# "programming is easy" string is

result = text.endswith('is', 7, 26)
print(result)  # Returns False

result = text.endswith('easy', 7, 26)
print(result)  # returns True

# endswith() With Tuple Suffix
result = text.endswith(('programming', 'python'))
# prints False
print(result)

# expand tabs
str = "xyz\t12345\tabc"
print('Original String:', str)

# tabsize is set to 2
print('Tabsize 2:', str.expandtabs(2))
# tabsize is set to 3
print('Tabsize 3:', str.expandtabs(3))
# tabsize is set to 4
print('Tabsize 4:', str.expandtabs(4))

# find
c = x.find("is")
print("Substring 'is':", c)
quote = 'Do small things with great love'

# if value is false it will give -1
# Substring is searched in 'hings with great love'
print(quote.find('small things', 10))

print(x.islower())
print(x.isalpha())
print(x.isalnum())
print(x.isidentifier())
print(x.istitle())
print(x.isupper())
print(x.isspace())
print(x.isprintable())
print(x.swapcase())

# split
x = x.split()
print(x)

# join method
print(' '.join(x))

# strip
string = ' Hi hello Hello   '
# Leading whitespace are removed
print(string.strip())
print(string.strip('he'))

# partition
string = "Python is fun"
# 'is' separator is found
print(string.partition('is '))

# replace
print(string.replace('python', 'Python'))
song = 'Let it be, let it be, let it be, let it be'
print(song.replace('let', "don't let", 2))  # only two occurrence's of 'let' is replaced
