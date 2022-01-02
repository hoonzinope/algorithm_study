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
    def traverse_temp(self, root: 'Optional[Node]'):
        while root != None:
            print(root.val, root.left, root.right, end=" ")
            root = root.next
        print()
    
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if root == None:
            return root
        
        node_list = []
        index = 0
        node_list.append(root)
        while node_list[index].left != None and node_list[index].right != None:
            node_list.append(node_list[index].left)
            node_list.append(node_list[index].right)
            index+=1
        
        curr = Node()
        head = Node()
        order = 0
        count = 1
        for index, node in enumerate(node_list):
            node.left = None
            node.right = None
            node.next = None
            if count == 1:
                curr = node
                head = curr
            else:
                curr.next = node
                curr = curr.next
            order += 1
            if order == count:
                if index != len(node_list)-1:
                    curr.next = Node(val="#", left=None, right=None, next = None)
                    curr = curr.next
                    order = 0
                    count *= 2
        
        return head