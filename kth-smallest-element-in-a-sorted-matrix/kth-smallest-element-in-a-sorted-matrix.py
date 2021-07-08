class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        num_list = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                num_list.append(matrix[i][j])
                
        num_list = sorted(num_list)
        return num_list[k-1]