n=int(input())
l=[[] for i in range(n)]
for i in range(n):
    l[i].append(input())
    l[i].append(input())
temp=input()
while(temp):
    for i in range(n):
        if l[i][0]==temp:
            print(temp+"="+l[i][1])
            break
    else:print("Not found")
    temp=input()

