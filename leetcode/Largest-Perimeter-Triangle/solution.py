class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums)
        m = 0
        for i in range(len(nums)-1, 1, -1):
            c = nums[i]
            for j in range(i, 1, -1):
                b = nums[j-1]
                a = nums[j-2]
                if a+b > c:
                    return a+b+c
        return m