class Solution:
    def minPartitions(self, n: str) -> int:
        n = [int(al) for al in n]
        count = 0
        while n.count(0) != len(n):
            for i in range(len(n)):
                if n[i] != 0:
                    n[i] = n[i]-1
            count += 1
        return count
        