class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return nums[0]
        
        length = len(nums) // 2
        new_nums = list(sorted(nums))
        
        count = 1
        for i in range(1,len(new_nums)):
            if new_nums[i-1] != new_nums[i]:
                if count > length:
                    return new_nums[i-1]
                else:
                    count = 1
            else:
                count += 1
                
        if count > length:
            return new_nums[-1]
