class Solution:
    def largestInteger(self, num: int) -> int:
        even_ = []
        odd_ = []
        
        num = [i for i in str(num)]
        for n in num:
            if int(n) % 2 == 0:
                even_.append(n)
            else:
                odd_.append(n)
                
        even_ = sorted(even_, reverse=True)
        odd_ = sorted(odd_, reverse=True)
        
        for i in range(len(num)):
            if int(num[i]) % 2 == 0:
                num[i] = even_.pop(0)
            else:
                num[i] = odd_.pop(0)
        
        return int("".join(num))