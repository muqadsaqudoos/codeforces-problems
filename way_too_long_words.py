n=int(input())
for i in range(n):
    c=input()
    a=len(c)
    count=0
    if a>10:
        print(c[0],end='')
        for i in range(1,a-1):
            count+=1
        print(count,end='')
        print(c[-1])
    else:
        print(c)
