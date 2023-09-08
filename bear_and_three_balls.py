n=int(input())
t=list(map(int,input().split()))
t.sort()
t2=[]
sen=-1
flag=False
for i in range(len(t)-1):
    if t[i]!=sen:
        for j in range(i+1,len(t)):
            if t[i]==t[j]:
                t[j]=sen
for i in range(len(t)):
    if t[i]!=sen:
        t2.append(t[i])
for i in range(len(t2)-2):
    if t2[i]+1==t2[i+1] and t2[i+1]+1==t2[i+2]:
        print('YES')
        flag=True
        break
if flag==False:
    print('NO')
