# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def parentReturn(node, nodeVal):
            if node == None:
                return None
            if node.val == nodeVal.val:
                return [node]
            else:
                temp_list = []
                temp_list = parentReturn(node.right, nodeVal)
                if temp_list == None:
                    temp_list = parentReturn(node.left, nodeVal)
                if temp_list == None:
                    return None
                else:
                    temp_list = [node] + temp_list
                
                return temp_list
            
        p_p = parentReturn(root, p)
        q_p = parentReturn(root, q)
        answer = None
        for x,y in zip(p_p, q_p):
            if x.val == y.val:
                answer = x
        return answer