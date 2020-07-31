#7/31/20
"""
Problem Statement:
Suppose an arithmetic expression is given as a binary tree. Each leaf is 
an integer and each internal node is one of '+', '−', '∗', or '/'.
Given the root to such a tree, write a function to evaluate it.
For example, given the following tree:
    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).
"""
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self, root):
        self.root = Node(root)
        
    def preOrderTraversal(self, current, traversal):
        #Recursive method to list each node using pre-order traversal and evaluate
        #each node with children upon completion of all recursion through that node.
        #Pre-order traversal order would be [*,+,3,2,+,4,5]
        if current is not None: 
            traversal.append(str(current.value))
            traversal = self.preOrderTraversal(current.left, traversal) #Traverse left 1 node
            traversal = self.preOrderTraversal(current.right, traversal) #Traverse right 1 node
            
            if current.left is not None and current.right is not None: #If current node has any children
            #Remove last 3 objects from traversal list and use eval function on them in
            #the following order: second, first, third. 
                evaluateNode = traversal[-3:]
                del traversal[-3:]
                traversal.append(eval(str(evaluateNode[1]) + str(evaluateNode[0]) + str(evaluateNode[-1])))
                
        return traversal
    
#Create tree by populating with nodes:        
tree = Tree("*")
tree.root.left = Node("+")
tree.root.right = Node("+")
tree.root.left.left = Node(3)
tree.root.left.right = Node(2)
tree.root.right.left = Node(4)
tree.root.right.right = Node(5)

#Call function to solve as expression tree using pre-order traversal and print solution:
traversal = tree.preOrderTraversal(tree.root, []) #Returns list with a single object.
print(traversal[0]) #Prints 45


#Testing out a non-full (a.k.a. improper) binary tree.
# 5/9 * 2 + 3 = 10/9 + 3 = 4.11
"""
   +
  / \
 3   *
    / \
  '/'   2 
  / \
 5   9
"""

tree2 = Tree("+")
tree2.root.left = Node(3)
tree2.root.right = Node("*")
tree2.root.right.left = Node("/")
tree2.root.right.right = Node(2)
tree2.root.right.left.left = Node(5)
tree2.root.right.left.right = Node(9)

traversal2 = tree2.preOrderTraversal(tree2.root, [])
print(traversal2[0]) #Prints 4.11
