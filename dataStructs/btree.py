# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# @param A : root node of tree
# @return a list of list of integers
class Node:
 
    # A utility function to create a new node
    def __init__(self, key):
        self.val = key 
        self.left = None
        self.right = None

def levelOrder(A):
    q = []
    out = []
    
    q.append(A)
    
    while len(q) > 0:
        level = len(q)
        a = []
        while level > 0:
            node = q[0]
            a.append(node.val)
            
            if node.left is not None:
                q.append(node.left) 

            if node.right is not None:
                q.append(node.right)

            q.pop(0)
            level -= 1
        
        out.append(a)
    return out
            
# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

levelOrder(root)
        
