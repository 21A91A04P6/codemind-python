t=int(input())
for i in range(t):
    m,n=map(int,input().split())
    count=0
    for j in range(m,n+1):
        r=j%10
        if(r==2 or r==3 or r==9):
            count+=1
    print(count)