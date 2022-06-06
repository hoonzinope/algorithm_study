# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        memA = []
        curr = headA
        while curr != None:
            memA.append(curr)
            curr = curr.next
        memA.reverse()
        
        memB = []
        curr = headB
        while curr != None:
            memB.append(curr)
            curr = curr.next
        memB.reverse()
        
        node = None
        for x,y in zip(memA,memB):
            if x!=y:
                return node
            else:
                node = x
        return node