class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_dict = {}
        for num in nums:
            if num not in num_dict:
                num_dict[num] = num
                
        for num in num_dict.keys():
            if num_dict[num] == num:
                temp_num = num+1
                while temp_num in num_dict:
                    num_dict[temp_num] = num_dict[num]
                    temp_num += 1
            else:
                continue
        
        temp_list = [[key, value] for key, value in num_dict.items()]
        num_dict = {}
        for info in temp_list:
            if info[1] not in num_dict:
                num_dict[info[1]] = 1
            else:
                num_dict[info[1]] += 1
        max_length = 0
        for num in num_dict:
            if num_dict[num] > max_length:
                max_length = num_dict[num]
        return max_length