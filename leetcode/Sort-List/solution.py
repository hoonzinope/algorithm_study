# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        temp_list = []
        curr = head
        while curr != None:
            temp_list.append(curr)
            curr = curr.next
            
        temp_list = sorted(temp_list, key = lambda x : x.val)
        for i in range(len(temp_list)-1):
            temp_list[i].next = temp_list[i+1]
        temp_list[-1].next = None
        
        return temp_list[0]