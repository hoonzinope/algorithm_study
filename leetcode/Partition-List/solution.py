# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        val_list = []
        curr = head
        index = 0
        while curr != None:
            if curr.val < x:
                val_list.insert(index, curr.val)
                index += 1
            else:
                val_list.append(curr.val)
            curr = curr.next
        
        curr = head
        while curr != None:
            curr.val = val_list.pop(0)
            curr = curr.next
        
        return head