# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node_list = []
        curr = head
        while curr != None:
            node_list.append(curr)
            curr = curr.next
            
        node_list.remove(node_list[-n])
        
        if len(node_list) == 0:
            return None
        else:
            if n <= len(node_list):
                node_list[-n].next = node_list[-n+1]
            node_list[-1].next = None
            return node_list[0]