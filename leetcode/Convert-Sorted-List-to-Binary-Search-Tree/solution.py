# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        num_list = []
        curr = head
        while curr != None:
            num_list.append(curr.val)
            curr = curr.next
        
        def dfs(nums):
            if len(nums) == 0:
                return None
            elif len(nums) == 1:
                return TreeNode(val=nums[0], left=None, right=None)
            else:
                left = 0
                right = len(nums)
                
                mid = (left+right) // 2
                
                if mid-1 >= 0:
                    left = dfs(nums[:mid])
                else:
                    left = None
                if mid+1 < len(nums):
                    right = dfs(nums[mid+1:])
                else:
                    right = None
                
                return TreeNode(val=nums[mid], left=left, right=right)
        return dfs(num_list)