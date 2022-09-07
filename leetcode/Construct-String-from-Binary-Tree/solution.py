# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        def dfs(node):
            noval = str(node.val)
            if node.left == None and node.right == None:
                return "("+noval+")"
            elif node.left != None and node.right == None:
                return "("+noval+dfs(node.left)+")"
            elif node.right != None and node.left == None:
                return "("+noval+"()"+dfs(node.right)+")"
            else:
                return "("+noval+dfs(node.left)+dfs(node.right)+")"
            
        return dfs(root)[1:-1]