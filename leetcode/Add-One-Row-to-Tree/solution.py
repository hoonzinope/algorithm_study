# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        prev_node_list = []
        node_list = [root]
        for i in range(depth-1):
            temp_list = []
            for node in node_list:
                if node.left:
                    temp_list.append(node.left)
                if node.right:
                    temp_list.append(node.right)
            prev_node_list = node_list
            node_list = temp_list
        
        if len(prev_node_list) == 0:
            temp_node = TreeNode(val=val, left=root, right=None)
            root = temp_node
        for node in prev_node_list:
            if node.left:
                temp_node = TreeNode(val=val, left=node.left, right=None)
                node.left = temp_node
            else:
                temp_node = TreeNode(val=val, left=None, right=None)
                node.left = temp_node
                
            if node.right:
                temp_node = TreeNode(val=val, left=None, right=node.right)
                node.right = temp_node
            else:
                temp_node = TreeNode(val=val, left=None, right=None)
                node.right = temp_node
                
        return root