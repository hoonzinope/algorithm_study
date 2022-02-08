class Solution:
    def repeatAdd(self, num):
        if num < 10:
            return num
        else:
            sum_num = 0
            num_str = str(num)
            for n in num_str:
                sum_num += int(n)
            
            return self.repeatAdd(sum_num)
        
    def addDigits(self, num: int) -> int:
        
        result = self.repeatAdd(num)
        return result