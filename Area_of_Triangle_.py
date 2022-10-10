a,b,c=map(int,input().split())
s=(a+b+c)/2
ar=s*(s-a)*(s-b)*(s-c)
d=ar**(0.5)
print("%0.2f"% round(d,2))
