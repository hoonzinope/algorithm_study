class Solution:
    def dfs(self, nums):
        if len(nums) == 1:
            return [nums]
        else:
            result = []
            for i in range(len(nums)):
                num = nums[i]
                temp_nums = list(nums[:i]+nums[i+1:])
                temp_result = self.dfs(temp_nums)
                for j in range(len(temp_result)):
                    temp_result[j] = [num]+temp_result[j]
                result.extend(temp_result)
            return result
            
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        result = self.dfs(nums)
        tempSet = set()
        for r in result:
            tempSet.add(tuple(r))
        result = []
        for t in tempSet:
            result.append(list(t))
            
        return result