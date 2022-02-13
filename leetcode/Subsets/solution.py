class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        result.append(list())
        for i in range(len(nums)):
            num = nums[i]
            temp_result = []
            for subSet in result:
                temp_set = list(subSet)
                temp_set.append(num)
                temp_result.append(temp_set)
            result.extend(temp_result)
            
        return result