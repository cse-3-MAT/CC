s=list(input())
temp=1
while temp!=0:
    temp=0
    c=len(s)
    for i in range(c-1):
        if s[i]==s[i+1]:
            s[i]=""
            s[i+1]=""
    s="".join(s)
    if len(s)==c:
        if c==0:print("Empty String")
        else:print(s)
    else:
        temp=1
        s=list(s)