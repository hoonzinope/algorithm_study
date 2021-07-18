# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        num_list = []
        while head.next:
            num_list.append(head.val)
            head = head.next
        num_list.append(head.val)
        
        reverse_num = len(num_list) // k
        start = 0
        end = k
        modi_list = []
        for _ in range(reverse_num):
            for index in range(end-1, start-1, -1):
                modi_list.append(num_list[index])
            if end+k > len(num_list):
                break
            start += k
            end += k
        
        modi_list.extend(num_list[end:len(num_list)])
        
        head = ListNode(modi_list[0], None)
        for index in range(1, len(modi_list)):
            node = ListNode(modi_list[index], None)
            
            temp_node = head
            while temp_node.next != None:
                temp_node = temp_node.next
            temp_node.next = node
        
        return head