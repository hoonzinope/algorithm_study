# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        num_list = []
        
        curr = head
        while True:
            if curr == None:
                return False
            
            if curr not in num_list:
                num_list.append(curr)
                curr = curr.next
            else:
                return True    