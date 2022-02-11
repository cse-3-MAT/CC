s = input()
a = True
l = []
for i in range(0,len(s)):
    for j in range(i,len(s)):
        if s[j] in s[i:j]:
            l.append(len(s[i:j]))
            a = False
            break
if a == True:
    print(len(s))
else:
    print(max(l))

