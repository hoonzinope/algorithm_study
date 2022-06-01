class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [nums[0]]
        for n in nums[1:]:
            result.append(result[-1]+n)
        return result