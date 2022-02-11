'''def wiggle(l):
    lst=[]
    for i in range(0,len(l)-1):
        if l[i+1]-l[i]!=0:lst.append(l[i+1]-l[i])
        else:return False

    if lst[0]>0:temp=1
    else:temp=-1
    for i in range(1,len(lst)):
        if lst[i]>0:
            c=1
        else:
            c=-1

        if c!=temp:
            temp=c
        else:return False
    return True

l=list(map(int,input().split()))
l1=[[]]
for i in l:
    l1+=[j+[i] for j in l1 ]
temp=[]
for i in l1:

    if len(i)>1 and  wiggle(i):temp.append(len(i))
print(max(temp))'''


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