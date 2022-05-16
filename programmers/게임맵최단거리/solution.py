def solution(maps):
    answer = 0
    
    if maps[0][0] == 0:
        return -1
    else:
        node_list = []
        node_list.append([0,0])
        
        n = len(maps)
        m = len(maps[0])
        
        visited = set()
        visited.add((0,0))
        
        while True:
            answer += 1
            if [n-1, m-1] in node_list:
                break
            
            temp_list = []
            for node in node_list:
                x = node[0]
                y = node[1]
                
                if x-1 >=0 and maps[x-1][y] == 1 and (x-1,y) not in visited:
                    visited.add((x-1,y))
                    temp_list.append([x-1,y])
                if x+1 < n and maps[x+1][y] == 1 and (x+1,y) not in visited:
                    visited.add((x+1,y))
                    temp_list.append([x+1,y])
                if y-1 >= 0 and maps[x][y-1] == 1 and (x, y-1) not in visited:
                    visited.add((x,y-1))
                    temp_list.append([x,y-1])
                if y+1 < m and maps[x][y+1] and (x,y+1) not in visited:
                    visited.add((x,y+1))
                    temp_list.append([x,y+1])
                    
            if len(temp_list) == 0:
                answer = -1
                break
            else:
                node_list = temp_list
                    
                
        
    return answer