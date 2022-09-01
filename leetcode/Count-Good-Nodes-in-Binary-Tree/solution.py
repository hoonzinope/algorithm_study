# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxNum):
            count = 0
            if node.val >= maxNum:
                count+=1
                maxNum = node.val
            
            
            if node.left != None:
                count += dfs(node.left, maxNum)
            if node.right != None:
                count += dfs(node.right, maxNum)
            
            return count
        
        count = dfs(root, root.val)
        return count