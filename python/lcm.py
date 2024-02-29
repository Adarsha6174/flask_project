a=12
b=18
great=0
ans=0
if a>b:
    great=a
else:
    great=b
c=True
d=1
while(c):
    if d%a==0 and d%b==0:
        c=False
        break
    d+=1
print(f'LCM is : {d}')
for i in range(1,great+1):
    if a%i==0 and b%i==0:
        ans=i
print(f'GCD is {ans}')
