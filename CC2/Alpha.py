class Node:
    def _init_(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def _init_(self):
        self.head = None
    def insert(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head
            while(temp.next is not None):
                temp = temp.next
            temp.next = Node(data)
    def Vowel(self):
        s = ['a','e','i','o','u','A','I','O','E','U']
        temp = self.head
        while(temp is not None):
            if temp.data in s:
                print(temp.data)
            temp = temp.next
    def cons(self):
        s = ['a', 'e', 'i', 'o', 'u', 'A', 'I', 'O', 'E', 'U']
        temp = self.head
        while (temp is not None):
            if temp.data not in s:
                print(temp.data)
            temp = temp.next
a = list(map(str,input().split()))
a.sort()
o = LinkedList()
for i in range(len(a)):
    o.insert(a[i])
o.Vowel()
o.cons()
