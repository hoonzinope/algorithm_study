class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp_dict = {}
        for num in nums:
            if num in temp_dict:
                temp_dict[num]+=1
            else:
                temp_dict[num] = 1
        
        for key, value in temp_dict.items():
            if value == 1:
                return key