class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        mat = []
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append(0)
            mat.append(temp)
        
        i = 0
        j = 0
        direction = "right"
        for num in range(1, n ** 2 +1):
            mat[i][j] = num
            if direction == "right":
                if j+1 <= n-1 and mat[i][j+1] == 0:
                    j+=1
                else:
                    direction = "down"
                    i+=1
            elif direction == "down":
                if i+1 <= n-1 and mat[i+1][j] == 0:
                    i+=1
                else:
                    direction = "left"
                    j-=1
            elif direction == "left":
                if j-1 >= 0 and mat[i][j-1] == 0:
                    j-=1
                else:
                    direction = "up"
                    i-=1
            else: #direction == "up"
                if i-1 >= 0 and mat[i-1][j] == 0:
                    i-=1
                else:
                    direction = "right"
                    j+=1
        return mat