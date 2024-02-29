from itertools import combinations
list=[10,2,3,4,5,9,7,8]
comb=combinations(list,4)
count=0
for i in comb:
    # if sum(i)==23:
    print(i)
        