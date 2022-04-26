# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def binSearch(self, num_list, num):
        left = 0
        right = len(num_list)
        while left < right:
            mid = (left + right) // 2
            if num_list[mid] == num:
                return mid
            else:
                if num_list[mid] < num:
                    left = mid+1
                else:
                    right = mid
        return left
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if len(lists) == 0:
            return None
        
        temp_list = []
        for head in lists:
            curr = head
            while curr != None:
                index = self.binSearch(temp_list, curr.val)
                temp_list.insert(index, curr.val)
                curr = curr.next
        
        if len(temp_list) == 0:
            return None
        
        answer = ListNode(next=None, val = temp_list[0])
        curr = answer
        for i in range(1, len(temp_list)):
            temp_node = ListNode(next = None, val = temp_list[i])
            curr.next = temp_node
            curr = curr.next
        
        return answer