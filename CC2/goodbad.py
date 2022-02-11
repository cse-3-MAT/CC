for i in range(int(input())):
    n,x=map(int,input().split())
    l=list(set(list(map(int,input().split()))))
    if len(l)>x:print("Average")
    elif x==len(l):print("Good")
    else:print("Bad")
