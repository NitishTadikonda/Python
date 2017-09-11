pyg = 'ay'

original = raw_input('Enter a word:')
word=original.lower()
first=word[0]
new_word=word+first+pyg
a = 1:len(new_word)
print(a)
if len(original) > 0 and original.isalpha():
  print original
else:
  print 'empty'
