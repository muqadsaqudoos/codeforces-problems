a=int(input())
n=int(input())
sum=0
count=0
c=a//2
i=1
while(i<=c):
    n=n//10
    e=d%10
    if e==4 or e==7:
        count+=1
    sum=sum+e
    i=i+1
j=1
sum1=0
while(j<=c):
    n=n//10
    e=d%10
    if e==4 or e==7:
        count+=1
    sum1=sum1+e
    j=j+1
if(sum==sum1 and count==a):
    print('YES')
else:
    print('NO')
    
    
