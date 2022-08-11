# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if node == None:
                return [[], True]
            else:
                mid = node.val
                left = dfs(node.left)
                right = dfs(node.right)
                flag = True
                if left[1] == False or right[1] == False:
                    flag = False
                elif len(left[0]) != 0 and left[0][1] >= mid:
                    flag = False
                elif len(right[0]) != 0 and right[0][0] <= mid:
                    flag = False
                
                total_num_list = left[0]+right[0]
                total_num_list.append(mid)
                min_num = min(total_num_list)
                max_num = max(total_num_list)
            
            return [[min_num, max_num], flag]
        
        return dfs(root)[1]