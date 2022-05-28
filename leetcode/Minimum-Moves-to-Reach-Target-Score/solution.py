class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        
        count = 0
        while target != 1:
            if target % 2 == 0:
                if maxDoubles > 0:
                    target //= 2
                    maxDoubles -= 1
                else:
                    count += target-1
                    target -= target-1
                    break
            else:
                if maxDoubles > 0:
                    target -= 1
                else:
                    count += target-1
                    target -= target-1
                    break
            count += 1
        return count