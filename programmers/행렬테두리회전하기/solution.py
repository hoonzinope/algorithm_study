def shaking(mat, query):
    
    x1,y1,x2,y2 = query
    x1,y1,x2,y2 = x1-1, y1-1, x2-1, y2-1
    
    curr = [x1,y1]
    insert = mat[curr[0]][curr[1]]
    min_num = 99999
    while True:
        if min_num > insert:
            min_num = insert
        # for i in range(len(mat)):
        #     for j in range(len(mat[0])):
        #         print(mat[i][j], end="\t")
        #     print()
        # print()

        if curr[0] == x1 and curr[1] != y2: 
            extract = mat[curr[0]][curr[1]+1]
            mat[curr[0]][curr[1]+1] = insert
            insert = extract
            curr = [curr[0], curr[1]+1]
            # print(curr, insert)
            continue
        if curr[1] == y2 and curr[0] != x2:
            extract = mat[curr[0]+1][curr[1]]
            mat[curr[0]+1][curr[1]] = insert
            insert = extract
            curr = [curr[0]+1, curr[1]]
            # print(curr, insert)
            continue
        if curr[0] == x2 and curr[1] != y1:
            extract = mat[curr[0]][curr[1]-1]
            mat[curr[0]][curr[1]-1] = insert
            insert = extract
            curr = [curr[0], curr[1]-1]
            # print(curr, insert)
            continue
        if curr[1] == y1 and curr[0] != x1:
            extract = mat[curr[0]-1][curr[1]]
            mat[curr[0]-1][curr[1]] = insert
            insert = extract
            curr = [curr[0]-1, curr[1]]
            # print(curr, insert)

            if curr[0] == x1 and curr[1] == y1:
                break
            else:
                continue
    
    
    return mat, min_num

def solution(rows, columns, queries):
    answer = []
    
    matrix = []
    num = 1
    for i in range(rows):
        temp_row = []
        for j in range(columns):
            temp_row.append(num)
            num += 1
        matrix.append(temp_row)
        
    for query in queries:
        matrix, min_num = shaking(matrix, query)
        answer.append(min_num)
    
    return answer