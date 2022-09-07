"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        node_vals = []
        if root:
            node_list = [root]
            flag = True
            while len(node_list) != 0:
                temp_list = []
                node_temp_list = []
                for node in node_list:
                    temp_list.append(node.val)

                    if len(node.children):
                        node_temp_list.extend([child for child in node.children if child])
                node_vals.append(temp_list)
                node_list = node_temp_list
            
        return node_vals