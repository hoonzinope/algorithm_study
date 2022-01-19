# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp_list = []
        curr = head
        while curr != None:
            if curr.next == None:
                return None
            else:
                if curr in temp_list:
                    return curr
                else:
                    temp_list.append(curr)
                    curr = curr.next
            
        return None