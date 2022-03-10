# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # num1 
        num1_list = []
        while l1.next:
            num1_list.append(l1.val)
            l1 = l1.next
        num1_list.append(l1.val)
        
        # num2
        num2_list = []
        while l2.next:
            num2_list.append(l2.val)
            l2 = l2.next
        num2_list.append(l2.val)
        
        range_n = 0
        long_n = 0
        if len(num1_list) < len(num2_list):
            range_n = len(num1_list)
            long = num2_list
        else:
            range_n = len(num2_list)
            long = num1_list
        
        add_num = 0
        answer_list = []
        for index in range(range_n):
            val = num1_list[index] + num2_list[index] +add_num
            answer_list.append(val%10)
            add_num = val//10
        
        for index in range(range_n, len(long)):
            val = long[index]+add_num
            answer_list.append(val%10)
            add_num = val//10
            
        if add_num != 0:
            answer_list.append(add_num)
            
        result = ListNode(answer_list[0], None)
        cur = result
        for index in range(1, len(answer_list)):
            new_node = ListNode(answer_list[index], None)
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node
        
        return result