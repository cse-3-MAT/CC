for _ in range(int(input())):
    s=input()
    n=False
    l=[]
    for i in range(0,len(s)):
        print(1)
        for j in range(i,len(s)):
            if s[j] in s[i:j]:
                l.append(len(s[i:j]))
                n=True
                break
    if n==False:
        l.append(len(s))
    print(max(l))   
