class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        elif n == 1:
            return [0,1]
        else:
            idx = 0
            result = [0,1]
            for i in range(2,n+1):
                if (i & (i-1)) == 0:
                    idx = 0
                    result.append(result[idx]+1)
                else:
                    result.append(result[idx]+1)
                idx += 1
        # print(result)
        return result