class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        al_dict = {}
        
        for i in range(ord('A'), ord('Z')+1):
            al_dict[chr(i)] = i-64
        
        result = 0
        for i, alpha in enumerate(columnTitle):
            result += al_dict[alpha] * (26 ** (len(columnTitle)-1-i))
        return result;