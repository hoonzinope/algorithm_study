# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self, node, k):
        temp_dict = {}
        temp_dict['list'] = []
        temp_dict['num'] = -1
        
        if node.left != None:
            temp_dict = self.inOrder(node.left, k)
            if temp_dict['list'] != None and len(temp_dict['list']) >= k:
                return temp_dict
            
        temp_dict['list'].append(node.val)
        if temp_dict['list'] != None and len(temp_dict['list']) >= k:
            temp_dict['num'] = temp_dict['list'][k-1]
            return temp_dict
        
        if node.right != None:
            right_dict = self.inOrder(node.right, k)
            temp_dict['list'].extend(right_dict['list'])
            if temp_dict['list'] != None and len(temp_dict['list']) >= k:
                temp_dict['num'] = temp_dict['list'][k-1]
                return temp_dict
            
        return temp_dict
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        temp_dict = self.inOrder(root, k)
        return temp_dict['num']