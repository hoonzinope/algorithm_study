# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        if root == None:
            return self.count
        def dfs(node, nums):
            if node.left == None and node.right == None:
                for i in range(len(nums)):
                    nums[i] = nums[i]+node.val
                    if nums[i] == targetSum:
                        self.count += 1
                nums.append(node.val)
                if nums[-1] == targetSum:
                    self.count += 1
            else:
                for i in range(len(nums)):
                    nums[i] = nums[i]+node.val
                    if nums[i] == targetSum:
                        self.count += 1
                nums.append(node.val)
                if nums[-1] == targetSum:
                    self.count += 1
                    
                if node.left != None:
                    dfs(node.left, list(nums))
                if node.right != None:
                    dfs(node.right, list(nums))
        
        dfs(root, [])
        return self.count