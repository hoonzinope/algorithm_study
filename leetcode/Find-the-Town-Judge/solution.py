class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        trust_list = []
        for _ in range(n):
            trust_list.append([0,0])
        
        for tr in trust:
            trust_list[tr[0]-1][0] = 1
            trust_list[tr[1]-1][1] += 1
            
        for index, tr in enumerate(trust_list):
            if tr[0] == 0 and tr[1] == (n-1):
                return index+1
        return -1