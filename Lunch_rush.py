n,k=map(int,input().split())
joy=0
for i in range(n):
    f,t=map(int,input().split())
    if i==0:
        if t>k:
            joy=f-(t-k)
        elif t<=k:
            joy=f
    elif i>0:
        if t>k and joy < f-(t-k):
            joy=f-(t-k)
        elif t<=k and joy < f:
            joy=f
print(joy)
