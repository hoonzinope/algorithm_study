class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        r = len(matrix)-1
        for i in range(len(matrix)):
            if matrix[i][0] > target:
                r = i-1
                break
            elif matrix[i][0] == target:
                r = i
                break
        
        
        left = 0
        right = len(matrix[r])
        while left < right:
            mid = (left+right) // 2
            if matrix[r][mid] == target:
                return True
            else:
                if matrix[r][mid] > target:
                    right = mid
                elif matrix[r][mid] < target:
                    left = mid+1
        return False