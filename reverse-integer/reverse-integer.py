class Solution:
    def reverse(self, x: int) -> int:
        
        n_str = [n for n in str(x).replace("-","")]
        n_str.reverse()
        n = int("".join(n_str))
        if x < 0:
            n *= -1
        
        if n > 2**31-1 or n < -2**31:
            return 0
        else:
            return n
