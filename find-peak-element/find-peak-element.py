class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            if left == right:
                return left
            
            if left > 0 and right < len(nums)-1:
                if nums[left] > nums[left-1] and nums[left] > nums[left+1]:
                    return left
                else:
                    left += 1
                
                if nums[right] > nums[right-1] and nums[right] > nums[right+1]:
                    return right
                else:
                    right -= 1
            else:
                if left == 0 and nums[left] > nums[left+1]:
                    return left
                else:
                    left += 1

                if right == len(nums)-1 and nums[right] > nums[right-1]:
                    return right
                else:
                    right -= 1