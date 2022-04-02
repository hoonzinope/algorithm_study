# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        length = 0
        curr = head
        while curr != None:
            curr = curr.next
            length += 1
        
        num_list = []
        curr = head
        for i in range(length//2):
            num_list.append(curr.val)
            curr = curr.next
        
        max_num = 0
        for i in range(length // 2):
            if num_list[-1-i] + curr.val > max_num:
                max_num = num_list[-1-i] + curr.val
            curr = curr.next
        
        return max_num