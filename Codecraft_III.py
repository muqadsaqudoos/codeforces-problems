months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
n=input()
k=int(input())
index=-1
for i in range(len(months)):
    if n==months[i]:
        index=i
        break
index+=k
i=0
count=0
while i<len(months):
    if count==index:
        print(months[i])
        break
    count+=1
    i+=1
    if i==12:
        i=0
