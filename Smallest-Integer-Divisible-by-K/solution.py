class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2== 0 or k % 5 == 0:
            return -1
        else:
            length = 1
            r = 1
            while True:
                r = r % k
                if r == 0:
                    return length
                else:
                    length += 1
                    r = ((10*r) + 1)