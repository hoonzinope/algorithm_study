# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return head
        
        count = 0
        curr = head
        node_list = []
        while curr != None:
            node_list.append(curr)
            curr = curr.next
            count += 1
        
        if k < count:
            node_list = node_list[-k:]+node_list[:-k]
            prev = node_list[0]
            for node in node_list[1:]:
                temp_node = ListNode(val=node.val, next=None)
                prev.next = temp_node
                prev = prev.next
        else:
            node_list = node_list[-(k%count):]+node_list[:-(k%count)]
            prev = node_list[0]
            for node in node_list[1:]:
                temp_node = ListNode(val=node.val, next=None)
                prev.next = temp_node
                prev = prev.next
        
        return node_list[0]