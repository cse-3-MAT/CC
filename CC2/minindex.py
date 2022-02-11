l = list(map(int,input().split()))
m = []
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if l[i]==l[j]:
            m.append(abs(i-j))
print(min(m))

