# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, Node):
        if Node == None:
            return []
        else:
            node_list = []
            if Node.left != None:
                node_list.extend(self.dfs(Node.left))
            
            if Node.right != None:
                node_list.extend(self.dfs(Node.right))
            
            result = []
            if len(node_list) == 0:
                result.append(str(Node.val))
            else:
                for node in node_list:
                    result.append(str(Node.val)+"->"+node)
            
            return result
            
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        result_list = self.dfs(root)
        
        return result_list