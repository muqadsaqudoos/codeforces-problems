t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    a=a-1
    b=b-c
    if b<0:
        b=-b
    b=b+c-1
    if a<b:
        print(1)
    elif b<a:
        print(2)
    else:
        print(3)
