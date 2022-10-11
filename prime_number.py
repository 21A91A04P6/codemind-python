n=int(input())
sum=0
for i in range(2,n//2):
    if(n%i==0):
        sum+=1
if(sum==0):
    print("prime")
else:
    print("not a prime")