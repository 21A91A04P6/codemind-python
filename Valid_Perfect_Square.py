t=int(input())
for i in range(t):
    f=0
    a=int(input())
    for j in range(a):
        if(a==j*j):
            f=1
    if(f==1):
        print("True")
    else:
        print("False")