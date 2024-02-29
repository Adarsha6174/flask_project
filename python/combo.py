from itertools import combinations
list=[10,2,3,4]
comb=combinations(list,3)
count=0
for i in comb:
    print(i,end=' ' )
        