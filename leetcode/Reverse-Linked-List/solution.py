# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        prev = None
        while curr != None:
            if prev == None:
                prev = curr
                if curr.next == None:
                    break
                curr = curr.next
                prev.next = None
            else:
                r_next = curr.next
                curr.next = prev
                prev = curr
                if r_next == None:
                    break
                curr = r_next
                
        return curr