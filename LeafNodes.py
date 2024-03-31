
#https://leetcode.com/problems/find-leaves-of-binary-tree/
#TC: O(n)
#SC: O(h)
#This makes use of the height to add elements to output list. We don't need removal, we just need to 
#add elements as per their height
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    global output
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.output=[]
        self.DFS(root,-1)
        return self.output
    def DFS(self, node, height):
        #Base
        if node is None:
            return height
        #Logic
        left = self.DFS(node.left,height)
        right = self.DFS(node.right,height)
        height=max(left,right)+1
        if len(self.output)==height:
            self.output.append([])
        self.output[height].append(node.val)
        return height
        
#https://hackerrank.com/challenges/tree-height-of-a-binary-tree/problem
#Computing Height
class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    return DFS(root, -1)

def DFS(node, height):
    #Base
    if node is None:
        return height
    #Logic
    left=DFS(node.left,height)
    right=DFS(node.right,height)
    height = max(left, right)+1
    return height



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print(height(tree.root))


#Computing Depth:
#https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.DFS(root,0)
    def DFS(self,node,dept):
        #base
        if node is None:
            return dept
        #Logic
        left=self.DFS(node.left,dept+1)
        right=self.DFS(node.right,dept+1)
        return max(left,right)


