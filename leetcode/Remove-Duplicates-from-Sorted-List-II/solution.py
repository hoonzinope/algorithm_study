# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp_dict = {}
        
        curr = head
        while curr != None:
            num = curr.val
            if num in temp_dict:
                temp_dict[num] += 1
            else:
                temp_dict[num] = 1
            curr = curr.next
        
        prev = None
        toad = None
        for num, val in temp_dict.items():
            if val > 1:
                continue
            else:
                node = ListNode(val=num, next=None)
                if toad == None:
                    toad = node
                    
                if prev != None:
                    prev.next = node
                prev = node
                
        return toad