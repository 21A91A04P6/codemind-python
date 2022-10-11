n=int(input())
sum=0
s=n*n
while(s!=0):
    r=s%10
    sum=sum+r
    s=s//10
if(sum==n):
    print("Neon Number")
else:
    print("Not Neon Number")