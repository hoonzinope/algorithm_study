class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] > target:
                    right = mid
                else:
                    left = mid+1
        
        return -1