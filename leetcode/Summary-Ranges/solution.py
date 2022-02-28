class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        result = []
        if len(nums) == 0:
            return []
        else:
            start = 0
            end = 0
            for i in range(1,len(nums)):
                if nums[i-1]+1 == nums[i]:
                    end += 1
                else:
                    # print(start, end, nums[start:end+1])
                    if start == end:
                        result.append(str(nums[start]))
                    else:
                        result.append(str(nums[start])+"->"+str(nums[end]))
                    start = end+1
                    end = start
            if start == end:
                result.append(str(nums[start]))
            else:
                result.append(str(nums[start])+"->"+str(nums[end]))
            
            return result