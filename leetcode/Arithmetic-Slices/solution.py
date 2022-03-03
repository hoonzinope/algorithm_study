class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        result = 0
        idx = 0
        for i in range(len(nums)-2):
            add_num = 3
            while True:
                end_idx = idx+add_num
                if end_idx > len(nums):
                    cal_num = add_num - 2 - 1
                    result += (cal_num+1)*cal_num/2
                    break
                    
                temp_nums = nums[idx:end_idx]
                # print(temp_nums)
                if sum(temp_nums) == (len(temp_nums) * (temp_nums[0]+temp_nums[-1]) / 2):
                    add_num+=1
                else:
                    cal_num = add_num - 2 - 1
                    result += (cal_num+1)*cal_num/2
                    # print(cal_num, result)
                    break
            idx = end_idx-2
            
        return int(result)