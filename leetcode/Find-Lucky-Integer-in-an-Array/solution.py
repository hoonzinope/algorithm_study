class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky_num = -1
        num_dict = dict()
        for num in arr:
            if num in num_dict:
                num_dict[num]+=1
            else:
                num_dict[num] =1
        
        for num in num_dict:
            if num == num_dict[num]:
                if lucky_num < num:
                    lucky_num = num
        
        return lucky_num