a,b,c=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=list(map(int,input().split()))
while(sum(l1)!=sum(l2)!=sum(l3)):
    if sum(l1)>sum(l2):l1.pop(0)
    if sum(l2)>sum(l3):l2.pop(0)
    if sum(l3)>sum(l1):l3.pop(0)
print(sum(l2))
