class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(nums)
        def binSearch(nums, target, direction):
            index = None
            left = 0
            right = len(nums)
            while left < right:
                mid = (left+right) // 2
                if nums[mid] == target:
                    index = mid
                    if direction == "l":
                        right -= 1
                    else:
                        left += 1
                else:
                    if nums[mid] < target:
                        left = mid+1
                    else:
                        right = mid
            return index
        
        l = binSearch(nums, target, "l")
        r = binSearch(nums, target, "r")
        answer = []
        if l != None and r != None:
            answer = [num for num in range(l,r+1)]
        return answer