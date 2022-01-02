# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num_list = []
        while head != None:
            num_list.append(head.val)
            head = head.next
        
        mid = (len(num_list) // 2)
            
        root = ListNode()
        curr = root
        for index, n in enumerate(num_list[mid:]):
            curr.val = n
            if(index == len(num_list[mid:])-1 ):
                break
            curr.next = ListNode()
            curr = curr.next
        
        return root