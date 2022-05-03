class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        sort_nums = sorted(nums)
        
        start_index = -1
        end_index = -1
        for i in range(len(nums)):
            if nums[i] != sort_nums[i]:
                if start_index == -1:
                    start_index = i
                end_index = i
        
        if start_index == end_index:
            return 0
        else:
            return end_index - (start_index-1)