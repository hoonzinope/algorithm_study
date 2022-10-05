# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        
        def dfs(node, depth):
            if node.left == None and node.right == None:
                return depth
            else:
                left = float("inf")
                if node.left != None:
                    left = dfs(node.left, depth+1)
                right = float("inf")
                if node.right != None:
                    right = dfs(node.right, depth+1)
                
                return min([left, right])
        
        if root == None:
            return 0
        else:
            return dfs(root, 1)