arr=[4,5,0,-2,-3,1]
N=5
all=[]
def sol(arr,k,N):
    list=[]
    start=0
    end=k
    while(end<=len(arr)):
        if sum(arr[start:end])%5==0:
            list.append(arr[start:end])
        end=end+1
        start+=1
    return list
for i in range(1,len(arr)+1):
    all=all+sol(arr,i,N)
print(all)