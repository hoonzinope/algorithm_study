class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # print(matrix[0])
        # print([r[0] for r in matrix])
        
        def binSearch(nums, num):
            left = 0
            right = len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] == num:
                    return mid
                else:
                    if nums[mid] < num:
                        left = mid+1
                    else:
                        right = mid
            return left
        
        col = binSearch(matrix[0], target)
        if col < len(matrix[0]) and matrix[0][col] == target:
            return True
        
        first_col = [r[0] for r in matrix]
        row = binSearch(first_col, target)
        if row < len(first_col) and first_col[row] == target:
            return True
        
        answer = False
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == target:
                    answer = True
        return answer