l=list(map(int,input().split()))
if l[0]>l[1]:temp=1
else:temp=-1
ans=1
for i in range(1,len(l)-1):
    if l[i]>l[i+1]:c=1
    else:c=-1
    if c!=temp:
        ans+=1
        temp=c
print(ans+1)
