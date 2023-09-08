t=int(input())
for i in range(t):
    a,b=input()
    c,d=input()
    count=0
    if a==b and b==c and c==d:
        count=0
    else:
        if (b==c and c==d) or (a==c and c==d) or (a==b and b==d) or (a==b and b==c):
            count+=1
        elif(a==b and c==d) or (a==d and b==c) or (a==c and b==d) :
            count+=1
        elif (a==b and b!=c) or (a==c and b!=d) or (a==d and b!=c) or (b==c and a!=d) or (b==d and a!=c) or (c==d and a!=b):
            count+=2
        else:
             count+=3
    print(count)
