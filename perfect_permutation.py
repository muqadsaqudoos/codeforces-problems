n=int(input())
a=2
b=a-1
if(n%2!=0):
    print('-1')
else:
    i=1
    while(i<=n/2):
        print(f'{a} {b}',end=' ')
        a=a+2
        b=a-1
        i=i+1
        
        
