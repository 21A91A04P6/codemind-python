n=int(input())
f=0
for i in range(n):
    for j in range(n):
        if(n==(i*i)+(j*j)):
            f=1
if(f==1):
    print("True")
else:
    print("False")