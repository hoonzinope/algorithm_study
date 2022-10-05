# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        
        left = 0
        if root.left!=None:
            left = root.left.val
        
        right = 0
        if root.right != None:
            right = root.right.val
            
        if root.val != (left+right):
            return False
        else:
            return True