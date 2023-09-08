n=int(input())
i=1
count=0
while(i<=n):
        a=input()
        end=' '
        b=input()
        end=' '
        c=input()
        end=' '
        a=int(a)
        b=int(b)
        c=int(c)
        if(a==1 and b==1):
            count+=1
        elif(a==1 and c==1):
            count+=1
        elif(b==1 and c==1):
            count+=1
        i=i+1
print(count)
            
