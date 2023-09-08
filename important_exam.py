n,m=map(int,input().split())
list=[]
a=[]
for i in range(n):
    list.append(input())
for i in range(n):
    for j in range(m):
        a.append(list[i][j])
         
  
print(a)
