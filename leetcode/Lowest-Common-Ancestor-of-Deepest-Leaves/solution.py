# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, depth):
            if node.left == None and node.right == None:
                return {"node" : node, "depth" : depth}
            elif node.left == None:
                return dfs(node.right, depth+1)
            elif node.right == None:
                return dfs(node.left, depth+1)
            else:
                left = dfs(node.left, depth+1)
                right = dfs(node.right, depth+1)
                
                if left['depth'] < right['depth']:
                    return right
                elif left['depth'] > right['depth']:
                    return left
                else:
                    return {'node' : node, "depth" : left['depth']}
        return dfs(root, 0)["node"]