n,k,l=map(int,input().split())
count=0
for i in range(n,k+1):
    if(i%l==0):
        count+=1
print(count)