def marcsCakewalk(calorie):
    # Write your code here
    calorie = sorted(calorie,reverse=True)
    s = 0
    i = 0
    for x in calorie:
        s += (2**i)*x
        i += 1
    return s
n = int(input())
l = list(map(int,input().split()))
print(marcsCakewalk(l))
