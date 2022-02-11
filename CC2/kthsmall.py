class Node:
     
    def __init__(self, key):
         
        self.data = key
        self.left = None
        self.right = None
 
# Recursive function to insert an key into BST
def insert(root, x):
     
    if (root == None):
        return Node(x)
    if (x < root.data):
        root.left = insert(root.left, x)
    elif (x > root.data):
        root.right = insert(root.right, x)
    return root
 
# Function to find k'th largest element
# in BST. Here count denotes the number
# of nodes processed so far
def kthSmallest(root):
     
    global k
     
    # Base case
    if (root == None):
        return None
 
    # Search in left subtree
    left = kthSmallest(root.left)
 
    # If k'th smallest is found in
    # left subtree, return it
    if (left != None):
        return left
         
    # If current element is k'th
    # smallest, return it
    k -= 1
    if (k == 0):
        return root
 
    # Else search in right subtree
    return kthSmallest(root.right)
def kthLargest(root):
     
    global k
    print(k)
    # Base case
    if (root == None):
        return None
 
    # Search in left subtree
    right = kthLargest(root.right)
 
    # If k'th smallest is found in
    # left subtree, return it
    if (right != None):
        return right
         
    # If current element is k'th
    # smallest, return it
    k -= 1
    if (k == 0):
        return root
 
    # Else search in right subtree
    return kthLargest(root.left)
 
# Function to find k'th largest element in BST
def printKthSmallLarge(roots,temp):
     
    # Maintain index to count number
    # of nodes processed so far
    
    count = 0
    res = kthSmallest(roots)
    if (res == None):
        print("There are less than k nodes in the BST")
    else:
        print("K-th Smallest Element is ", res.data)
    k=temp
    res = kthLargest(roots)
    if (res == None):
        print("There are less than k nodes in the BST")
    else:
        print("K-th Largest Element is ", res.data)

# Driver code
if __name__ == '__main__':
     
    root = None
    keys = list(map(int,input().split()))
 
    for x in keys:
        root = insert(root, x)
 
    k =int(input("enter value of k : "))
     
    printKthSmallLarge(root,k)