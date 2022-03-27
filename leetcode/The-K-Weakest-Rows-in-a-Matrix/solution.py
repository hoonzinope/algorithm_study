class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        temp = []
        for i in range(len(mat)):
            # if sum(mat[i]) <= sum(mat[i+1]):
            temp.append([i, sum(mat[i])])
        
        temp = sorted(temp, key=lambda x : x[1])
        result = []
        for i in range(k):
            result.append(temp[i][0])
            
        return result