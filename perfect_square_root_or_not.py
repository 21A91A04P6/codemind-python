a=int(input())
f=0
for i in range(1,a):
    d=i
    if((a/i)==d):
        f=1
if(f==1):
    print('True')
else:
    print('False')