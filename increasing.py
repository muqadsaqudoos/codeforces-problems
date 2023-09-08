t=int(input())
for i in range(t):
    n=int(input())
    count=0
    a=list(map(int,input().split()))
    for i in range(n):
        for j in range(i+1,n):
            if a[i]==a[j]:
                count=1
    if count==1:
        print("NO")
    else:
        print("YES")
