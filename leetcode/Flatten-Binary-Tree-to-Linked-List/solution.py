# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return None
        else:
            left = None
            if root.left != None:
                left = self.flatten(root.left)
            right = None
            if root.right != None:
                right = self.flatten(root.right)
            if left != None:
                curr = left
                while curr.right != None:
                    curr = curr.right
                
                curr.right = right
                root.left = None
                root.right = left
            return root
    
            