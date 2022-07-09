class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        max_list = [nums[0]]
        result=[nums[0]]
        
        def binInsert(nums, num):
            left = 0
            right = len(nums)
            while left < right:
                mid = (left+right)//2
                if nums[mid] == num:
                    return mid
                else:
                    if nums[mid] < num:
                        left = mid+1
                    else:
                        right = mid
            return left
        
        
        for i in range(1,len(nums)):
            # print(result, max_list)
            if len(result) <= k:
                max_num = max_list[-1]+nums[i]
                result.append(max_num)
                max_list.insert(binInsert(max_list, max_num), max_num)
            else:
                max_list.pop(binInsert(max_list,result[i-k-1]))
                max_num = max_list[-1]+nums[i]
                result.append(max_num)
                max_list.insert(binInsert(max_list, max_num), max_num)
        return result[-1]