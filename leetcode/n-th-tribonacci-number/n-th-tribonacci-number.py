class Solution:
    def tribonacci(self, n: int) -> int:
        num_list = [0,1,1]
        if n < len(num_list):
            return num_list[n]
        else:
            num = 0
            for i in range(2,n):
                num = num_list[i-2] + num_list[i-1] + num_list[i]
                num_list.append(num)
            return num_list[n]