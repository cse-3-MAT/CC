l=[1,2,3]
target = int(input())
s=[[]]
for i in l:
    s+=[[i]+j for j in s]
print(s)
l1 = []
for i in s:
    if sum(i)==target and i not in l1:
        l1.append(i)

print(l1)


