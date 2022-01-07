# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    import random
    head = None
    length = 0
    
    def __init__(self, head: Optional[ListNode]):
        self.head = head
        curr = head
        while curr != None:
            curr = curr.next
            self.length+=1
        # print(self.length)
        return None

    def getRandom(self) -> int:
        curr = self.head
        if self.length == 1:
            return curr.val
        else:
            idx = self.random.randrange(1,self.length+1)
            for i in range(idx-1):
                curr = curr.next
            return curr.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()