t=int(input())
count=0
for i in range(t):
    n=int(input())
    s=input()
    for j in range(n):
        if s[j]=='Q':
            count+=1
        else:
            count-=1
        if count<=0:
            count=0
    if(count==0):
        print('Yes')
    else:
        print('No')
        count=0
            
