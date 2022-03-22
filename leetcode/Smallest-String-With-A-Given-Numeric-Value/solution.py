class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        alpha_dict = {}
        for i in range(97, 97+26):
            alpha_dict[i-96] = chr(i)
        
        result = []
        for i in range(n, 0, -1):
            if k-(i-1) > 26:
                result.append(26)
                k -= 26
            else:
                result.append(k- (i-1))
                k -= k- (i-1)
        
        result = reversed(result)
        result = "".join([ alpha_dict[k] for k in result])
        return result