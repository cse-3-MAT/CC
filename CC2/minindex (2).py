n=int(input())
l=list(map(int,input().split()))
d=[]
for i in range(n):
    if l[i] in l[:i]:
        for j in range(i):
            if l[i]==l[j]:d.append(abs(i-j))
if len(d)==0:print(-1)
else:print(min(d))