# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        temp_list = []
        curr = head
        flag = False
        prevNode = None
        nextNode = None
        index = 1
        while curr != None:
            if index == left:
                flag = True
                temp_list.append(curr)
            
            if index == right:
                flag = False
                temp_list.append(curr)
                nextNode = curr.next
                break
            else:
                if flag == True:
                    temp_list.append(curr)
            if flag == False:
                prevNode = curr
            curr = curr.next
            index += 1
        
        if prevNode != None:
            prevNode.next = temp_list[-1]
        else:
            head = temp_list[-1]
        for i in range(len(temp_list)-1, 0, -1):
            temp_list[i].next = temp_list[i-1]
        temp_list[0].next = nextNode
        
        return head