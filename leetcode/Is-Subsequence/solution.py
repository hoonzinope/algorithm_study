class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = 0
        for alpha in s:
            # print(alpha, idx, t)
            if alpha in t:
                idx = t.index(alpha)+1
                t = t[idx:]
            else:
                return False
            
        return True