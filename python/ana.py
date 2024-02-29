a='silent'
b='listen'
count=0
for i in a:
    if a.count(i)==b.count(i):
        count+=1
if count==len(a):
    print('Anagram')
else:
    print('Not Anagram')