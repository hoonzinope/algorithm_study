class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        result = []
        for j in range(len(matrix[0])):
            temp_list = []
            for i in range(len(matrix)):
                temp_list.append(matrix[i][j])
            result.append(temp_list)
        return result