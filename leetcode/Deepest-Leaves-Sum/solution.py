# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, step):
        if node.left == None and node.right == None:
            return [node.val, step]
        else:
            left_node = None
            if node.left != None:
                left_node = self.dfs(node.left, step+1)
            
            right_node = None
            if node.right != None:
                right_node = self.dfs(node.right, step+1)
            
            if left_node != None and right_node != None:
                if left_node[1] > right_node[1]:
                    return left_node
                elif left_node[1] == right_node[1]:
                    return [left_node[0]+right_node[0], right_node[1]]
                else:
                    return right_node
            elif left_node == None:
                return right_node
            else:
                return left_node
            
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        node_info = self.dfs(root, 0)
        return node_info[0]