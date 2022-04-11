class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        row_num = len(grid)
        col_num = len(grid[0])
        
        num_list = []
        for row in grid:
            for num in row:
                num_list.append(num)
        
        n = len(num_list)
        len_list = n
        while k >= len_list:
            len_list += n
        
        answer = []
        n = len_list - k
        num_list = num_list[n : ] + num_list[ : n]
        index = 0
        for i in range(row_num):
            temp_list = []
            for j in range(col_num):
                temp_list.append(num_list[index])
                index+=1
            answer.append(temp_list)
        
        return answer