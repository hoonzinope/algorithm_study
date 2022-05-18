def solution(m, n, board):
    answer = 0
    
    for i in range(m):
        board[i] = [n for n in board[i]]
    
    flag = True
    while flag:
        # remove
        remove_pos = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == 0:
                    continue
                if board[i][j] == board[i][j+1] and\
                board[i][j+1] == board[i+1][j+1] and\
                board[i+1][j+1] == board[i+1][j]:
                    remove_pos.add((i,j))
                    remove_pos.add((i+1,j))
                    remove_pos.add((i+1,j+1))
                    remove_pos.add((i,j+1))

        for pos in remove_pos:
            i = pos[0]
            j = pos[1]
            board[i][j] = 0
            
        # organize
        org_flag = False
        while True:
            for i in range(m):
                for j in range(n):
                    if board[i][j] == 0 and board[i-1][j] != 0:
                        if i > 0:
                            board[i-1][j],board[i][j] = board[i][j], board[i-1][j]
                            org_flag = True
            if org_flag == True:
                org_flag = False
                continue
            else:
                break
        # for i in range(m):
        #     for j in range(n):
        #         print(board[i][j], end="")
        #     print()
        # print()
        
        # valid
        if len(remove_pos) > 0:
            flag = True
            answer += len(remove_pos)
        else:
            flag = False        
    return answer