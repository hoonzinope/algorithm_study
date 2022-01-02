class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        module = [0]*60
        
        count = 0
        for n in time:
            if n % 60 == 0:
                count += module[n%60]
            else:
                count += module[60 - (n%60)]
            module[n%60] += 1
            # print(n, module[n%60], count)
        
        return count