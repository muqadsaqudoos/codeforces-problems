k=int(input())
l=int(input())
m=int(input())
n=int(input())
d=int(input())
i=1
count=0
while(i<=d):
    if(i%k==0 or i%l==0 or i%m==0 or i%n==0):
        count+=1
    i=i+1
print(count)
        
