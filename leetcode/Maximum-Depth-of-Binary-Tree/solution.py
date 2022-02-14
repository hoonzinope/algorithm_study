# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, depth):
        if node == None:
            return 0
        
        if node.left == None and node.right == None:
            return depth
        else:
            left_depth = 0
            right_depth = 0
            if node.left != None:
                left_depth = self.dfs(node.left, depth+1)
            if node.right != None:
                right_depth = self.dfs(node.right, depth+1)
                
            if left_depth > right_depth:
                return left_depth
            else:
                return right_depth
            
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        depth = self.dfs(root, 1)
        return depth