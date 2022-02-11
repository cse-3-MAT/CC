l=[]
for i in range(int(input())):
    l.append(input())
    l=list(set(l))
    print(len(l))