n=int(input())
ad=0
p=1
while(n):
    r=n%10
    ad+=r
    p*=r
    n=n//10
s=(p-ad)
print(s)