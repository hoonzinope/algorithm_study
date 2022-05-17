# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        node_list = []
        node_list.append(cloned)
        while True:
            temp_list = []
            for node in node_list:
                if node.val == target.val:
                    return node
                if node.left != None:
                    temp_list.append(node.left)
                if node.right != None:
                    temp_list.append(node.right)
            node_list = temp_list