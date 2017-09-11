x = open("Myfile1.txt").read().replace(',','').replace('\'','').replace('.','').replace('"','').split()
word = {}
for i in x:
    b = i.lower() or i.upper()
    if b in word:
        word[b] += 1
    else:
        word[b] = 1
print("The count of all the words:",sum(word.values()))
print("Word"+'\t'+"times")
for k,v in word.items():
    print(k+'\t'+str(v))
