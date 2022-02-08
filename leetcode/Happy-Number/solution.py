class Solution:
    def repeatAdd(self, num, sum_num_dict):
        num_str = str(num)
        sum_num = 0
        for n in num_str:
            sum_num += (int(n)**2)
        
        if sum_num == 1:
            return sum_num
        else:
            if sum_num in sum_num_dict:
                return -1
            else:
                sum_num_dict[sum_num] = True
                return self.repeatAdd(sum_num, sum_num_dict)
    
    def isHappy(self, n: int) -> bool:
        
        sum_num_dict = dict()
        result = self.repeatAdd(n, sum_num_dict)
        if result == 1:
            return True
        else:
            return False