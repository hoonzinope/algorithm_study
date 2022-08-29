class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        visited = []
        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(False)
            visited.append(temp)
        
        def back(i, j):
            visited[i][j] = True
            
            if i-1 >= 0 and grid[i-1][j] == "1" and visited[i-1][j] == False:
                back(i-1,j)
            if i+1 < m and grid[i+1][j] == "1" and visited[i+1][j] == False:
                back(i+1,j)
            if j-1 >= 0 and grid[i][j-1] == "1" and visited[i][j-1] == False:
                back(i,j-1)
            if j+1 < n and grid[i][j+1] == "1" and visited[i][j+1] == False:
                back(i,j+1)
            return
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and visited[i][j] == False:
                    count += 1
                    back(i,j)
              
        return count