n=int(input())
count=0
list=[]
sen=-1
for i in range(n):
    list.append(input().split())
for i in range(len(list)-1):
    if list[i]!=sen:
        for j in range(i+1,len(list)):
            if list[i]==list[j]:
                list[j]=sen
for i in range(len(list)):
    if list[i]!=sen:
        count+=1
        
    
print(count)
