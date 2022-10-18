class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        check = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    check.append((i,j))
                    
        for c in check:
            i = c[0]
            j = c[1]
            
            for n in range(len(matrix[i])):
                matrix[i][n] = 0
            for n in range(len(matrix)):
                matrix[n][j] = 0
        