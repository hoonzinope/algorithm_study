# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        list_length = 0
        curr = head
        while curr != None:
            list_length += 1
            curr = curr.next;
            
        temp = ""
        curr = head
        for i in range(list_length // 2):
            temp += str(curr.val)
            curr = curr.next
        
        if list_length % 2 != 0:
            curr = curr.next
        
        for i in range(list_length // 2):
            if temp[-1] == str(curr.val):
                temp = temp[:-1]
            else:
                return False
            curr = curr.next
        
        if temp == "":
            return True
        else:
            return False