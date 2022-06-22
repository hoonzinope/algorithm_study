class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [int(num) for num in nums]
        def binSearch(nums, num):
            left = 0
            right = len(nums)
            while left < right:
                mid = (left+right) // 2
                if nums[mid] == num:
                    return mid
                else:
                    if nums[mid] < num:
                        left = mid+1
                    else:
                        right = mid
            return left
        
        result = []
        for num in nums:
            index = binSearch(result, num)
            result.insert(index, num)
        return str(result[-k])