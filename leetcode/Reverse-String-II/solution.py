class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        s = [alpha for alpha in s]
        start = 0
        while start < len(s):
            end = start+k
            if end > len(s)-1:
                end = len(s)
            
            temp = ""
            if end < len(s)+1:
                temp = s[start:end]
                temp = temp[::-1]
                for i in range(start,end):
                    s[i] = temp[i-start]
            start = end+k
        
        return "".join(s)