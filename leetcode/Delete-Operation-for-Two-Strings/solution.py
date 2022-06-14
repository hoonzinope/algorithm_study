class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word2)
        m = len(word1)
        
        mat = [] 
        for i in range(n):
            row = []
            for j in range(m):
                row.append(0)
            mat.append(row)
            
        for i in range(n):
            for j in range(m):
                temp_list = []
                if i-1 >= 0 and j-1 >= 0:
                    temp_list.append(mat[i-1][j-1])
                if i-1 >= 0:
                    temp_list.append(mat[i-1][j])
                if j-1 >= 0:
                    temp_list.append(mat[i][j-1])
                
                max_num = 0
                if len(temp_list) != 0:
                    max_num = max(temp_list)
                
                if word2[i] == word1[j]:
                    if i-1 >= 0 and j-1 >= 0:
                        mat[i][j] = mat[i-1][j-1]+1
                    else:
                        mat[i][j] = 1
                else:
                    mat[i][j] = max_num
        count = 0   
        count += (n-mat[-1][-1])
        count += (m-mat[-1][-1])
        return count