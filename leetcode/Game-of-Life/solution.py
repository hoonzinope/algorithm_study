class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        temp_list = []
        for row in board:
            temp_list.append([x for x in row])
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                sub_i = []
                if i-1 >= 0:
                    sub_i.append(i-1)
                sub_i.append(i)
                if i+1 < len(board):
                    sub_i.append(i+1)

                sub_j = []
                if j-1 >= 0:
                    sub_j.append(j-1)
                sub_j.append(j)
                if j+1 < len(board[i]):
                    sub_j.append(j+1)

                count = 0
                for si in sub_i:
                    for sj in sub_j:
                        if si == i and sj == j:
                            continue
                        else:
                            if board[si][sj] == 1:
                                count += 1
                # print([i,j],sub_i, sub_j, count)
                
                if board[i][j] == 1:
                    if count < 2:
                        temp_list[i][j] = 0
                    elif count == 2 or count == 3:
                        continue
                    elif count > 3:
                        temp_list[i][j] = 0
                if board[i][j] == 0:
                    if count == 3:
                        temp_list[i][j] = 1
        
        for i in range(len(temp_list)):
            for j in range(len(temp_list[i])):
                board[i][j] = temp_list[i][j]
                    
                