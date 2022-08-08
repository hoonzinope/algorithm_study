class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        counts = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                counts[i] = 1
            else:
                for j in range(i):
                    if nums[j] < nums[i]:
                        counts[i] = max(counts[j]+1, counts[i])
        # print(counts)
        return max(counts)