# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            count = 0
            if node.left != None:
                c = dfs(node.left)
                if c == 0:
                    node.left = None
                else:
                    count += c
            if node.right != None:
                c = dfs(node.right)
                if c == 0:
                    node.right = None
                else:
                    count += c
            return node.val+count
        
        count = dfs(root)
        if count == 0:
            return None
        else:
            return root