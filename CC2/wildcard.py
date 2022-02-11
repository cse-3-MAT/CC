a = []
def genbin(s):
    if '?' in s:
        s1 = s.replace('?','0',1)
        s2 = s.replace('?','1',1)
        genbin(s1)
        genbin(s2)
    else:
        a.append(s)
s = input("enter any string\n")
genbin(s)
print(a)


