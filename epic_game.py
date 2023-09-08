def gcd(n,m):
    max1=0
    if(m>n):
        max1=m
    else:
        max1=n
    max2=0
    for i in range(1,max1+1):
        if(n%i==0 and m%i==0):
            max2=i
    return max2
a,b,n=map(int,input().split())
count=0
while (n!=0 and n>0):
    if(count!=2):
        x=gcd(a,n)
        n=n-x
        if(n==0):
            count=1
    if(count!=1):
        y=gcd(b,n)
        n=n-y
        if(n==0):
            count=2
        
if(count==1):
    print('0')
else:
    print('1')
