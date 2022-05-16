class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        count = 0
        visited = set()
        if grid[0][0] == 1:
            return -1
        else:
            node_list = []
            node_list.append([0,0])
            
            while True:
                count += 1
                
                if [len(grid)-1, len(grid)-1] in node_list:
                    return count
                
                temp_list = []
                #8path
                for node in node_list:
                    x = node[0]
                    y = node[1]
                    visited.add((x,y))
                    
                    if x-1 >= 0:
                        if y-1 > 0 and grid[x-1][y-1] == 0:
                            if (x-1,y-1) not in visited:
                                temp_list.append([x-1,y-1])
                                visited.add((x-1,y-1))
                                
                        if y+1 < len(grid) and grid[x-1][y+1] == 0:
                            if (x-1,y+1) not in visited:
                                temp_list.append([x-1,y+1])
                                visited.add((x-1,y+1))
                                
                        if grid[x-1][y] == 0:
                            if (x-1,y) not in visited:
                                temp_list.append([x-1,y])
                                visited.add((x-1,y))
                                
                    if x+1 < len(grid):
                        if y-1 > 0 and grid[x+1][y-1] == 0:
                            if (x+1,y-1) not in visited:
                                temp_list.append([x+1,y-1])
                                visited.add((x+1,y-1))
                                
                        if y+1 < len(grid) and grid[x+1][y+1] == 0:
                            if (x+1,y+1) not in visited:
                                temp_list.append([x+1,y+1])
                                visited.add((x+1,y+1))
                                
                        if grid[x+1][y] == 0:
                            if (x+1,y) not in visited:
                                temp_list.append([x+1,y])
                                visited.add((x+1,y))
                                
                    if y-1 > 0 and grid[x][y-1] == 0:
                        if (x,y-1) not in visited:
                            temp_list.append([x,y-1])
                            visited.add((x,y-1))

                    if y+1 < len(grid) and grid[x][y+1] == 0:
                        if (x,y+1) not in visited:
                            temp_list.append([x,y+1])
                            visited.add((x,y+1))
                print(temp_list)           
                if len(temp_list) == 0:
                    count = -1
                    break
                else:
                    node_list = temp_list
                    
            return count