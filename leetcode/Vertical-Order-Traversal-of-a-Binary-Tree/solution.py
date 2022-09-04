# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        temp_dict = {}
        
        def dfs(node, row, col):
            if (row, col) not in temp_dict:
                temp_dict[(row, col)] = [node.val]
            else:
                temp_dict[(row, col)].append(node.val)
                
            if node.left:
                dfs(node.left, row+1, col-1)
            if node.right:
                dfs(node.right, row+1, col+1)
        dfs(root, 0,0)
        items = [[key, sorted(value)] for key, value in temp_dict.items()]
        items = sorted(items, key = lambda x : (x[0][1], x[0][0], x[1]))
        
        temp_dict = {}
        for item in items:
            if item[0][1] not in temp_dict:
                temp_dict[item[0][1]] = item[1]
            else:
                temp_dict[item[0][1]].extend(item[1])
        items = [[key, value] for key, value in temp_dict.items()]
        items = sorted(items, key = lambda x : x[0])
        
        answer = []
        for item in items:
            answer.append(item[1])
        return answer
        
        