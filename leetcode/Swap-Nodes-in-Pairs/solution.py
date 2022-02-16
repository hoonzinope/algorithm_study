# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        even_flag = False
        curr = head
        prev = None
        prev_before = None
        start_flag = False
        start = None
        while curr != None:
            if even_flag == False:
                prev = curr
                curr = curr.next
                even_flag = True
            else:
                if start_flag == False:
                    start = curr
                    start_flag = True
                    
                if prev_before != None:
                    prev_before.next = curr
                    
                prev.next = curr.next
                curr.next = prev
                curr = prev.next
                
                prev_before = prev
                even_flag = False
        
        
        if start_flag == False:
            start = head
        return start