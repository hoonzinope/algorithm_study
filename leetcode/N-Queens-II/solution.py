class Solution:
    def totalNQueens(self, n: int) -> int:
        self.answer = 0
        board = [0]*n

        def valid(k):
            for i in range(k):
                if board[i] == board[k] or abs(i-k) == abs(board[i]-board[k]):
                    return False
            return True

        def back(k):
            if k == 0:
                for i in range(n):
                    board[k] = i
                    if valid(k):
                        if k == n-1:
                            self.answer += 1
                        else:
                            back(k+1)
                    board[k] = 0
            else:
                for i in range(n):
                    board[k] = i
                    if valid(k):
                        if k == n-1:
                            self.answer += 1
                        else:
                            back(k+1)
                    board[k] = 0
        back(0)
        return self.answer