n=int(input())
c=0
p=n
while(n>0):
    c+=1
    n=n//10
s=p**2
r=s%(10**c)
if(r==p):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")