# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root == None:
            return result
        node_list = [root]
        while len(node_list) != 0:
            temp_list = []
            child = []
            for node in node_list:
                temp_list.append(node.val)
                if node.left != None:
                    child.append(node.left)
                if node.right != None:
                    child.append(node.right)
            result.append(temp_list[-1])
            node_list = child
        return result