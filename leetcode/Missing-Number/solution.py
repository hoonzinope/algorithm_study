class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_num = 0
        for i in range(len(nums)+1):
            sum_num += i
        for n in nums:
            sum_num -= n
        return sum_num