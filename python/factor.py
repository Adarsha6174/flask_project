num1=int(input('Enter first number :'))
num2=int(input('Enter second number :'))
flist=[]
prime2=[]
def factors(num):
    factors=[]
    for i in range(1,num+1):
        if num%i==0:
            factors.append(i)
    flist.append(factors)
def prime(num):
    count=0
    prime=[]
    for i in num:
        for j in range(1,i+1):
            if i%j==0:
                count=count+1
        if count==2:
            prime.append(i)
    prime2.append(prime)
factors(num1)
factors(num2)
prime(flist)
print(flist)
print(prime2)