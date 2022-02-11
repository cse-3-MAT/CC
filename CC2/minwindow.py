s=list("this is a test string")
w=list("tist")
c=len(s)+1
def check(temp):
    for i in w:
        if i not in temp or w.count(i)!=temp.count(i):
            return False
    return True

for i in range(len(s)):
    for j in range(i,len(s)):
        if check(s[i:j+1]):
            if c>len(s[i:j+1]):
                c=len(s[i:j+1])
                res=''.join(s[i:j+1])
print(res)