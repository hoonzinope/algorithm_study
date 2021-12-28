class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for index,n in enumerate(nums):
            if n == val:
                nums[index] = 999
                count+=1
        length = len(nums) - count
        
        for i in range(len(nums[:-1])):
            for j in range(i, len(nums)):
                if i == j:
                    continue
                else:
                    if nums[i] > nums[j]:
                        temp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = temp
        
        
        return length