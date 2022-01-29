# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, Node):
        if Node.left == None and Node.right == None:
            return [str(Node.val)]
        else:
            node_values = []
            if Node.left != None:
                node_values.extend(self.dfs(Node.left))
            
            if Node.right != None:
                node_values.extend(self.dfs(Node.right))
                
            result = []
            for node in node_values:
                result.append(str(Node.val) + node)
                
            return result
        
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = self.dfs(root)
        result_num = 0
        for num_str in result:
            result_num += int(num_str)
        
        return result_num