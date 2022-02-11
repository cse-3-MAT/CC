l=list(map(int,input().split()))
temp=l.copy()
temp.sort()
for i in range(len(l)-1):
    if l[i+1:]+l[:i+1]==temp:
        print(l[i+1:][0])
        break
