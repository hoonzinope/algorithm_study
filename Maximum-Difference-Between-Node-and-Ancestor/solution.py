# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subTree_minmax(self, node : Optional[TreeNode]):
        this_min = node.val
        this_max = node.val
        this_sub = 0
        
        if node.left == None and node.right == None:
            # print(this_min, this_max, 0)
            return this_min, this_max, 0
        
        elif node.left == None and node.right != None:
            r_min, r_max, r_sub = self.subTree_minmax(node.right)
            if this_sub < abs(node.val - r_min):
                this_sub = abs(node.val - r_min)
            if this_sub < abs(node.val - r_max):
                this_sub = abs(node.val - r_max)
                
            this_min = min([r_min, r_max, node.val])
            this_max = max([r_min, r_max, node.val])
            
            if this_sub < r_sub:
                this_sub = r_sub
            # print(node.val, this_min, this_max, this_sub)
            return this_min, this_max, this_sub
        
        elif node.left != None and node.right == None:
            l_min, l_max, l_sub = self.subTree_minmax(node.left)
            if this_sub < abs(node.val - l_min):
                this_sub = abs(node.val - l_min)
            if this_sub < abs(node.val - l_max):
                this_sub = abs(node.val - l_max)
                
            this_min = min([l_min, l_max, node.val])
            this_max = max([l_min, l_max, node.val])
            
            if this_sub < l_sub:
                this_sub = l_sub
            # print(node.val, this_min, this_max, this_sub)
            return this_min, this_max, this_sub
        
        else:
            l_min, l_max, l_sub = self.subTree_minmax(node.left)
            r_min, r_max, r_sub = self.subTree_minmax(node.right)
            
            if this_sub < abs(node.val - l_min):
                this_sub = abs(node.val - l_min)
                
            if this_sub < abs(node.val - r_min):
                this_sub = abs(node.val - r_min)
                
            if this_sub < abs(node.val - l_max):
                this_sub = abs(node.val - l_max)
                
            if this_sub < abs(node.val - r_max):
                this_sub = abs(node.val - r_max)
                
            this_min = min([l_min,r_min,l_max,r_max,node.val])
            this_max = max([l_min,r_min,l_max,r_max,node.val])
            
            this_sub = max([this_sub, l_sub, r_sub])
            # print(node.val, this_min, this_max, this_sub)
            return this_min, this_max, this_sub
        
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        _,_,sub_max = self.subTree_minmax(root)
        return sub_max