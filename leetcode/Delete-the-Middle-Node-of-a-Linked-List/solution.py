# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        count = 0
        curr = head
        while curr != None:
            curr = curr.next
            count+=1
        
        index = count//2
        prev = None
        curr = head
        for i in range(index):
            prev = curr
            curr = curr.next
        if prev == None:
            return None
        else:
            prev.next = curr.next
        return head