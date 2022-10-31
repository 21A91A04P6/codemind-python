n=int(input())
temp=n
s=0
while(n!=0):
    n//=10
    s=s+1
q=temp**2
p=q%(10**s)
if(p==temp):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")