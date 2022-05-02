class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        
        odd = []
        even = []
        for i in range(len(nums)):
            if i % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        even = sorted(even)
        odd = sorted(odd, reverse=True)
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = even.pop(0)
            else:
                nums[i] = odd.pop(0)
        
        return nums