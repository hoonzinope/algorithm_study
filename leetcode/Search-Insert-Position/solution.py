class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[0] > target:
            return 0
        if nums[len(nums)-1] < target:
            return len(nums)
        
        l = 0
        r = len(nums)
        while True:
            mid = (l+r) // 2
            mid_num = nums[mid]
            if mid_num == target:
                return mid
            elif mid_num > target:
                if nums[mid-1] < target:
                    return mid
                else:
                    r = mid
            else: #mid_num < target:
                if nums[mid+1] > target:
                    return mid+1
                else:
                    l = mid