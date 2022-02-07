class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for alpha in s:
            t= t.replace(alpha,"",1)
        return t