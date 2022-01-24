# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, Node, targetSum):
        if Node == None:
            return None
        else:
            value_list = []
            if Node.left != None:
                left_list = self.dfs(Node.left, targetSum - Node.val)
                if left_list != None:
                    value_list.extend(left_list)
            if Node.right != None:
                right_list = self.dfs(Node.right, targetSum - Node.val)
                if right_list != None:
                    value_list.extend(self.dfs(Node.right, targetSum - Node.val))
            
            if len(value_list) == 0:
                if targetSum == Node.val and Node.left == None and Node.right == None:
                    return [[Node.val]]
                else:
                    return None
            else:
                for value in value_list:
                    if targetSum == (Node.val + sum(value)):
                        value.append(Node.val)
                return value_list
            
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        result_list = self.dfs(root, targetSum)
        answer = []
        if result_list != None:
            for result in result_list:
                if len(result) != 0:
                    answer.append(list(reversed(result)))
                    
        if len(answer) != 0:
            return True
        else:
            return False