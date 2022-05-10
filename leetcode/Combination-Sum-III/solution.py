class Solution:
    def dfs(self, step, k, nums, add_num, n):
        result = []
        if step == k:
            for num in nums:
                if add_num + num == n:
                    result.append([num])
            if len(result) != 0:
                return result
            else:
                return []
        else:
            for num in nums:
                if add_num + num < n:
                    index = nums.index(num)
                    temp_nums = nums[index+1:]
                    temp_result = self.dfs(step+1, k, temp_nums, add_num+num, n)
                    
                    if len(temp_result) == 0:
                        continue
                    else:
                        for temp in temp_result:
                            if temp != None:
                                temp.append(num)
                            result.append(temp)
            if len(result) != 0:
                return result
            else:
                return []
                
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        nums = [n for n in range(1, 10)]
        
        result = self.dfs(1,k,nums,0,n)
        return result