# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr != None:
            length += 1
            curr = curr.next
        
        prev_index = k
        next_index = length-(k-1)
        
        if prev_index == next_index:
            return head
        
        curr_index = 1
        curr = head
        
        prev_front = None
        front = None
        
        prev_rear = None
        rear = None
        
        prev = None
        while curr != None:
            if curr_index == prev_index:
                prev_front = prev
                front = curr
            elif curr_index == next_index:
                prev_rear = prev
                rear = curr
            prev = curr
            curr = curr.next
            curr_index += 1
        # front , rear switch
        if prev_front != None:
            prev_front.next = rear
        else:
            head = rear
        
        if prev_rear != None:
            prev_rear.next = front
        else:
            head = front
        front_next = front.next
        rear_next = rear.next
        rear.next = front_next
        front.next = rear_next
        
        return head