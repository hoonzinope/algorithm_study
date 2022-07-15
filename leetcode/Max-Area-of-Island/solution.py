class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = []
        for i in range(len(grid)):
            temp_list = [False] * len(grid[i])
            visited.append(temp_list)
        
        def bfs(i, j):
            temp_list = []
            if visited[i][j]:
                return 0
            else:
                temp_list.append((i,j))
                visited[i][j] = True
                count = 1
                
                while len(temp_list) != 0:
                    new_temp_list = []
                    for pos in temp_list:
                        y,x = pos[0], pos[1]
                        # up
                        if y-1 >= 0 and not visited[y-1][x] and grid[y-1][x] == 1:
                            new_temp_list.append((y-1,x))
                            visited[y-1][x] = True
                        # down
                        if y+1 < len(grid) and not visited[y+1][x] and grid[y+1][x] == 1:
                            new_temp_list.append((y+1,x))
                            visited[y+1][x] = True
                        # left
                        if x-1 >= 0 and not visited[y][x-1] and grid[y][x-1] == 1:
                            new_temp_list.append((y,x-1))
                            visited[y][x-1] = True
                        # right
                        if x+1 < len(grid[y]) and not visited[y][x+1] and grid[y][x+1] == 1:
                            new_temp_list.append((y,x+1))
                            visited[y][x+1] = True
                    temp_list = new_temp_list
                    count += len(temp_list)
                return count
                
        max_ = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1 and not visited[i][j]:
                    count = bfs(i,j)
                    if max_ < count:
                        max_ = count
        return max_