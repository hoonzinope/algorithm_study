"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        
        node_list = []
        curr = head
        while curr != None:
            node_list.append(curr)
            curr = curr.next
        
        new_node_list = []
        new_head = Node(x = node_list[0].val, next = None, random = None)
        prev = new_head
        new_node_list.append(prev)
        for i in range(1, len(node_list)):
            node = node_list[i]
            new_node = Node(x = node.val, next = None, random = None)
            prev.next = new_node
            prev = new_node
            new_node_list.append(prev)
        
        for i in range(len(node_list)):
            node = node_list[i]
            if node.random != None:
                random_idx = node_list.index(node.random)
                new_node_list[i].random = new_node_list[random_idx]
            else:
                new_node_list[i].random = None
        
        return new_node_list[0]