"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        node_list = []
        node_list.append(root)
        
        while True:
            temp_list = []
            for node in node_list:
                if node != None:
                    if node.left != None:
                        temp_list.append(node.left)
                    if node.right != None:
                        temp_list.append(node.right)
            
            for i in range(len(temp_list)-1):
                temp_list[i].next = temp_list[i+1]
                
            if len(temp_list) == temp_list.count(None):
                break
            
            node_list = temp_list
        return root