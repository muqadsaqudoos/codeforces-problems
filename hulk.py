n=int(input())
for i in range(n):
    if (i+1)%2!=0:
        print('I hate',end=' ')
        if (i+1)==n:
            print('it')
        else:
            print('that',end=' ')
    else:
        print('I love',end=' ')
        if (i+1)==n:
            print('it')
        else:
            print('that',end=' ')



#link for problem statement
#https://codeforces.com/contest/705/submission/179415609
