class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        cycle = [i for i in range(len(points))]
        
        edges = []
        for i in range(len(points)):
            for j in range(i, len(points)):
                x1 = points[i][0]
                y1 = points[i][1]
                
                x2 = points[j][0]
                y2 = points[j][1]
                
                if i == j:
                    continue
                else:
                    weight = abs(x1-x2) + abs(y1-y2)
                edges.append([i,j,weight])
        
        answer = 0
        edges = sorted(edges, key=lambda x : x[2])
        for edge in edges:
            if cycle[edge[0]] == cycle[edge[1]]:
                continue
            else:
                answer += edge[2]
                p1 = cycle[edge[0]]
                p2 = cycle[edge[1]]
                if p1 < p2:
                    for i in range(len(cycle)):
                        if cycle[i] == p2:
                            cycle[i] = p1
                else:
                    for i in range(len(cycle)):
                        if cycle[i] == p1:
                            cycle[i] = p2
                            
        return answer
        
        
        