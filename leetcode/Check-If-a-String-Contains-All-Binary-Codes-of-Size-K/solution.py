class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        num_set = set()
        
        for i in range(len(s)-(k-1)):
            num = int(s[i:i+k],2)
            num_set.add(num)
        
        if len(num_set) == 2**k:
            return True
        else:
            return False
        