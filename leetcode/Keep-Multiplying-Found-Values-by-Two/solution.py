class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        num_dict= {}
        for num in nums:
            if num not in num_dict:
                num_dict[num] = 1
        
        while original in num_dict:
            original *= 2
        
        return original