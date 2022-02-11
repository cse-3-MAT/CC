def sortedInsert(s, element):
    if len(s) == 0 or element > s[-1]:
        s.append(element)
        return
    else:
        temp = s.pop()
        sortedInsert(s, element)
        s.append(temp)
def sortStack(s):
    if len(s) != 0:
        temp = s.pop()
        sortStack(s)
        sortedInsert(s, temp)
s=[30,-5,18,14,-3]
print("Stack elements before sorting: ",s)
sortStack(s)
print("\nStack elements after sorting: ",s)
