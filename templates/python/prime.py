l=int(input())
r=int(input())
list=[]
a=0
prime=0
for i in range(l,r+1):
    print(i)
    if i<0:
        a=i
        i=abs(i)
    if i!=0 and 1:
        for j in range(2,(i//2)+1):
            if i%j==0:
                prime=1
    if prime==1 :
        prime=0
    else:
        if a<0 and i!=0 and i!=1:
            list.append(-i)
            prime=0
            a=0
        else: 
            if i!=0 and i!=1:
                list.append(i)
                prime=0
print(list)