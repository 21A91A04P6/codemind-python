n=int(input())
a=0
b=1
cout=0
for i in range(n+1):
    if(a==n):
        cout+=1
    c=a+b
    a=b
    b=c
if(cout==1):
    print("True")
else:
    print("False")