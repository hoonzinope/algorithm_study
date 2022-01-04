class Solution:
    def int2binary(self, num):
        temp = []
        while True:
            temp.append(num%2)
            num//=2
            if num == 0 or num == 1:
                break
        return temp
        
    def binary2int(self, num_list):
        total_num = 0
        for index, num in enumerate(num_list):
            if num == 0:
                num = 1
            else:
                num = 0
            total_num += ((2**index) * num)
        return total_num
        
    def bitwiseComplement(self, n: int) -> int:
        num_list = self.int2binary(n)
        return_num = self.binary2int(num_list)
        return return_num