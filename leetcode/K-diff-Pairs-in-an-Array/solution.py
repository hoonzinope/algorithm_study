class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        count = 0
        already_use_num = set()
        for i in range(len(nums)):
            num = nums[i]
            if num in already_use_num:
                continue
                
            nums_set = set(nums[i+1:]) - already_use_num
            if k == 0:
                if num in nums_set:
                    count+=1
            else:
                if num-k in nums_set:
                    count+=1
                if num+k in nums_set:
                    count+=1
            already_use_num.add(num)
        return count