class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        
        def binSearch(nums, num):
            left = 0
            right = len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] == num:
                    return mid
                else:
                    if nums[mid] < num:
                        left = mid+1
                    else:
                        right = mid
            return left
        
        index = binSearch(nums, target)
        if index >= len(nums) or nums[index] != target:
            return [-1,-1]
        else:
            left = 0
            for i in range(index, -1, -1):
                if nums[i] != target:
                    left = i+1
                    break
            right = len(nums)-1
            for i in range(index, len(nums)):
                if nums[i] != target:
                    right = i-1
                    break
                    
            return [left, right]