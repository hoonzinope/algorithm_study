def dfs(start = None, distance = None, mat = None, visited = None):
    if distance < 0:
        return None
        
    node_list = []
    for i, dist in enumerate(mat[start-1]):
        if dist == None:
            continue
        else:
            if distance - dist >= 0:
                if visited[i] == None:
                    node_list.append(i+1)
                    visited[i] = distance - dist
                else:
                    if distance - dist > visited[i]:
                        node_list.append(i+1)
                        visited[i] = distance - dist
    # print(start, node_list, visited)
    if len(node_list) > 0:
        for node in node_list:
            if mat[start-1][node-1] != None and mat[start-1][node-1] != 0:
                dist = distance - mat[start-1][node-1]
                dfs(start = node, distance = dist, mat = mat, visited = visited)
    else:
        return None

    return None

def solution(N, road, K):
    answer = 0

    mat = []
    for i in range(N):
        temp = []
        for j in range(N):
            if i == j:
                temp.append(0)
            else:
                temp.append(None)
        mat.append(temp)

    for info in road:
        start = info[0]
        end = info[1]
        dist = info[2]
        if mat[start-1][end-1] != None:
            if mat[start-1][end-1] > dist:
                mat[start-1][end-1] = dist
                mat[end-1][start-1] = dist
        else:
            mat[start-1][end-1] = dist
            mat[end-1][start-1] = dist

    visited = [None] * N
    dfs(start = 1, distance= K, mat = mat, visited = visited)
    for i, visit in enumerate(visited):
        if visit != None:
            answer += 1
    return answer
