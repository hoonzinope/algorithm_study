# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        root = ListNode("")
        curr = root
        while True:
            if list1 == None and list2 == None:
                break
            else:
                if list1 != None and list2 != None:
                    val1 = list1.val
                    val2 = list2.val
                    if val1 <= val2:
                        curr.val = val1
                        list1 = list1.next
                    else:
                        curr.val = val2
                        list2 = list2.next
                    curr.next = ListNode()
                    curr = curr.next
                elif list1 == None:
                    while list2 != None:
                        curr.val = list2.val
                        list2 = list2.next
                        if list2 != None:
                            curr.next = ListNode()
                            curr = curr.next
                elif list2 == None:
                    while list1 != None:
                        curr.val = list1.val
                        list1 = list1.next
                        if list1 != None:
                            curr.next = ListNode()
                            curr = curr.next
                        
        return root
                        
                        