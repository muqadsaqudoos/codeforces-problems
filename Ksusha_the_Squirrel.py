from time import *
n,k=map(int,input().split())
flag=True
a=list(input())
flag=True
i=1
s1=time()
while (i < len(a)):
    j=i
    count=0
    while a[j]=="#" :
        j+=1
        count+=1
        if count>=k:
            print("NO")
            flag=False
            break
    if flag==False:
        break
    i=j
    i+=1

if flag==True:
    print("YES")
s2=time()
print(s2-s1)
            
