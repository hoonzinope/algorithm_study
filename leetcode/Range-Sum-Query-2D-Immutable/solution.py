class NumMatrix:
    matrix = []
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        for i in range(len(matrix)):
            for j in range(1,len(matrix[i])):
                self.matrix[i][j] = (self.matrix[i][j] + self.matrix[i][j-1])
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum_num = 0
        for i in range(row1, row2+1):
            num = 0
            if col1-1 >= 0:
                col = col1-1
                num = self.matrix[i][col2] - self.matrix[i][col]
            else:
                num = self.matrix[i][col2]
            sum_num += num
        return sum_num

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)