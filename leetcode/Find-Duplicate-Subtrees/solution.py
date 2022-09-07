# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        node_info_dict = {}
        
        def dfs(node):
            noval = str(node.val)
            if node.left == None and node.right == None:
                noval = "("+noval+")"
            elif node.left == None:
                right_noval = dfs(node.right)
                noval = noval+"(_"+right_noval+")"
            elif node.right == None:
                left_noval = dfs(node.left)
                noval = noval+"("+left_noval+"_)"
            else:
                left_noval = dfs(node.left)
                right_noval = dfs(node.right)
                noval = noval+"("+left_noval+right_noval+")"
                
            if noval not in node_info_dict:
                node_info_dict[noval] = [node, 1]
            else:
                node_info_dict[noval][1] += 1
            return noval
                
        dfs(root)
        answer = []
        for key,value in node_info_dict.items():
            if value[1] > 1:
                answer.append(value[0])
                    
        return answer