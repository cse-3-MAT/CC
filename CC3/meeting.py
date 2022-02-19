class Meeting:
    def __init__(self,start,end):
        self.start = start
        self.end = end
def arrange(l):
    x = []
    x.append(0)
    t = l[0].end
    c = 1
    for i in range(1,len(s)):
        if l[i].start>t:
            x.append(i)
            c += 1
            t = l[i].end
    for i in x:
        print(i+1,end = ' ')
    print()    
    print(c)    
    
l = []
s = list(map(int,input().split()))
e = list(map(int,input().split()))
for i in range(len(s)):
    l.append(Meeting(s[i],e[i]))
arrange(l)    
