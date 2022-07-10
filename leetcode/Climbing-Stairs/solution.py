class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {}
        def td(n, stepCount):
            if n == 0:
                return stepCount
            else:
                count = 0
                if n in mem:
                    return mem[n]
                else:
                    if n >= 2:
                        count += td(n-2, stepCount)
                        count += td(n-1, stepCount)
                    elif n >= 1:
                        count += td(n-1, stepCount)
                        
                    if n not in mem:
                        mem[n] = count
                    return count
        count = 0
        for i in range(1,3):
            count += td(n-i, 1)
        return count