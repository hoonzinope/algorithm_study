# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        node_list = [root]
        answer_list = []
        while len(node_list) != 0:
            number_list = [node.val for node in node_list]
            answer_list.append(sum(number_list)/len(number_list))
            temp_list = []
            for node in node_list:
                if node.left:
                    temp_list.append(node.left)
                if node.right:
                    temp_list.append(node.right)
            node_list = temp_list
            
        return answer_list