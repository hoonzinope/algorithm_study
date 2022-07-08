class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = []
        for i in range(rowIndex+1):
            if i == 0:
                result.append([1])
            else:
                temp_list = []
                for j in range(i+1):
                    if j == 0 or j == i:
                        temp_list.append(1)
                    else:
                        temp_list.append(result[0][j-1]+result[0][j])
                result.pop()
                result.append(temp_list)
        return result[0]