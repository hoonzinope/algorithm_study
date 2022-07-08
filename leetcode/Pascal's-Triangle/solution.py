class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            if i == 0:
                result.append([1])
            else:
                temp_list = []
                for j in range(i+1):
                    if j == 0 or j == i:
                        temp_list.append(1)
                    else:
                        temp_list.append(result[i-1][j-1]+result[i-1][j])
                result.append(temp_list)
        return result