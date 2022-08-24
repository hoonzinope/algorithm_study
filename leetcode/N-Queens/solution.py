class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.answer = []
        board = [0]*n

        def valid(k):
            for i in range(k):
                if board[i] == board[k] or abs(i-k) == abs(board[i]-board[k]):
                    return False
            return True

        def draw(board):
            board_list = []
            for i in board:
                temp = ["."] * n
                temp[i] = "Q"
                board_list.append("".join(temp))
            self.answer.append(board_list)
        def back(k):
            if k == 0:
                for i in range(n):
                    board[k] = i
                    if valid(k):
                        if k == n-1:
                            draw(board)
                        else:
                            back(k+1)
                    board[k] = 0
            else:
                for i in range(n):
                    board[k] = i
                    if valid(k):
                        if k == n-1:
                            draw(board)
                        else:
                            back(k+1)
                    board[k] = 0
        back(0)
        return self.answer