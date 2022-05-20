class Solution:
    def dfs(self, board, i,j, visited):
        if board[i][j] == 1:
            visited[i][j] = 0
            return 0
        
        if len(board)-1 == i and len(board[0])-1 == j:
            visited[i][j] = 1
            return 1 #[[[i,j]]]
        else:
            down = 0 #[]
            if i+1 < len(board) and board[i+1][j] != 1:
                if visited[i+1][j] != 0:
                    down = visited[i+1][j]
                else:
                    down = self.dfs(board, i+1, j, visited)
                    visited[i+1][j] = down
            right = 0 #[]
            if j+1 < len(board[0]) and board[i][j+1] != 1:
                if visited[i][j+1] != 0:
                    right = visited[i][j+1]
                else:
                    right = self.dfs(board, i, j+1, visited)
            
            visited[i][j] = down+right
            return down+right#result
            
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        visited = []
        for _ in range(len(obstacleGrid)):
            temp = []
            for _ in range(len(obstacleGrid[0])):
                temp.append(0)
            visited.append(temp)
            
        result = self.dfs(obstacleGrid, 0, 0, visited)
        return result