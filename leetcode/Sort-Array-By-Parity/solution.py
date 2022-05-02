class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        index = 0
        while index < len(nums):
            if nums[index] % 2 == 0:
                num = nums.pop(index)
                nums.insert(0, num)
                index += 1
            else:
                index += 1
        
        return nums