n=int(input())
sum=0
for i in range(1,n):
    a=n%i
    if(a==0):
	    sum=sum+i
if(sum==n):
	print("True")
else:
	print("False")