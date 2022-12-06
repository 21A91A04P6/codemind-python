n=int(input())
s=0
c=0
p=0
temp=n
while(n!=0):
    r=n%10
    s=s*10+r
    n=n//10
for i in range(1,temp+1):
    if(temp%i==0):
        c+=1
for j in range(1,s+1):
    if(s%j==0):
        p+=1
if(p<3 and c<3):
    print("circular prime")
elif(c<3):
    print("prime but not a circular prime")
else:
    print("not prime")