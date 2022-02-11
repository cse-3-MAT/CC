def arrange(l):
    l1=[]
    l2=[]
    temp=["a",'e','i','o','u']
    for i in l:
        if i in temp:l2.append(i)
        else:l1.append(i)
    print(l1,l2)
    l1.sort()
    l2.sort()
    
    return [l2+l1]
for _ in range(int(input())):
    n1=int(input())
    print(arrange(list(map(str,input().split()))))
